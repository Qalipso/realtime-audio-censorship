#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the streaming API.
NOTE: This module requires the dependencies `pyaudio` and `termcolor`.
To install using pip:
    pip install pyaudio
    pip install termcolor
Example usage:
    python transcribe_streaming_infinite.py
"""

# [START speech_transcribe_infinite_streaming]
from censor_sound import SILENT_CHUNK
from constants import STREAMING_LIMIT, CHUNK_SIZE, STREAMING_CONFIG
from filter_vocabulary import censFilter
from resumable_mic_stream import audio_stream, mic_manager
import re
import time
from threading import Lock
import copy
import wave
# import json 
import math
import threading
from google.cloud import speech
import pyaudio

# Audio recording parameters



output_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=16000, output=True, frames_per_buffer=CHUNK_SIZE)
output_trans = []
censFilter.create()


def get_current_time():
    """Return Current Time in MS."""
    return int(round(time.time() * 1000))



def clear_old_audio():
    lock_clear = Lock()
    while True:
        time.sleep(100)
        lock_clear.acquire()
        try:
            audio_stream.input_audio_stream = []
        finally:
            lock_clear.release()  
        

def load_audio_stream():
    lock_load = Lock()
    while True:
        time.sleep(2)
        lock_load.acquire()
        try:  
            tmp = copy.copy(audio_stream.input_audio_stream[audio_stream.last_chunk:audio_stream.last_chunk+20])
            audio_stream.output_audio_stream.put(b"".join(tmp))
            [audio_stream.out_put.append(q) for q in tmp]
            audio_stream.last_chunk = audio_stream.last_chunk + 20
        finally:
            lock_load.release()         

def output():
    time.sleep(5)
    while True:
        if not audio_stream.output_audio_stream.empty():
            x = audio_stream.output_audio_stream.get()
            output_stream.write(x)   
        else:
            break

            

def listen_print_loop(responses, stream,lock):
    """Iterates through server responses and prints them.
    The responses passed is a generator that will block until a response
    is provided by the server.
    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    
    for response in responses:
        if get_current_time() - stream.start_time > STREAMING_LIMIT:
            stream.start_time = get_current_time()
            break

        if not response.results:
            continue

        result = response.results[0]

        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript.lower()

        result_seconds = 0
        result_micros = 0

        if result.result_end_time.seconds:
            result_seconds = result.result_end_time.seconds

        if result.result_end_time.microseconds:
            result_micros = result.result_end_time.microseconds

        stream.result_end_time = int((result_seconds * 1000) + (result_micros / 1000))

        corrected_time = (
            stream.result_end_time
            - stream.bridging_offset
            + (STREAMING_LIMIT * stream.restart_counter)
        )

        tmp = transcript.split(" ")[-1]
        print(tmp)
        if len(tmp)>2 and tmp not in censFilter.stopwords and (tmp in censFilter.vocabulary 
        or censFilter.lemmatizer.parse(tmp)[0].normal_form in censFilter.lem_voc 
        or censFilter.stemmer.stem(tmp) in censFilter.stem_voc): #censor words
            start_chunk = (math.floor(corrected_time/100) - 12) % 1000
            for i in range(start_chunk % 1000,(start_chunk + 3) % 1000):
                lock.acquire()
                try:
                    audio_stream.input_audio_stream[i] = SILENT_CHUNK
                finally:
                    lock.release() 
        
        if result.is_final: 
            stream.is_final_end_time = stream.result_end_time
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(выход|quit)\b", transcript, re.I):
            
                wf = wave.open('output.wav', 'wb')
                wf.setnchannels(1)
                sample_format = pyaudio.paInt16
                wf.setsampwidth(stream._audio_interface.get_sample_size(sample_format))
                wf.setframerate(stream._rate)
                wf.writeframes(b''.join(audio_stream.audio_wav))
                wf.close()
                wf = wave.open('output_res.wav', 'wb')
                wf.setnchannels(1)
                sample_format = pyaudio.paInt16
                wf.setsampwidth(stream._audio_interface.get_sample_size(sample_format))
                wf.setframerate(stream._rate)
                wf.writeframes(b''.join(audio_stream.input_audio_stream))
                wf.close()
                
                stream.closed = True
                break


def main():
    """start bidirectional streaming from microphone input to speech API"""
    lock = Lock()
    client = speech.SpeechClient()
    with mic_manager as stream:
        threading.Thread(name= 'out__put',target=output).start()
        threading.Thread(target=clear_old_audio,daemon=True).start()
        threading.Thread(target=load_audio_stream,daemon=True).start()
        while not stream.closed:

            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )
            responses = client.streaming_recognize(STREAMING_CONFIG, requests)
            
            # Now, put the transcription responses to use.
            listen_print_loop(responses, stream,lock)

            if stream.result_end_time > 0:
                stream.final_request_end_time = stream.is_final_end_time
            stream.result_end_time = 0
            stream.last_audio_input = []
            stream.last_audio_input = stream.audio_input
            stream.audio_input = []
            stream.restart_counter = stream.restart_counter + 1
            stream.new_stream = True

if __name__ == "__main__":
    main()

# [END speech_transcribe_infinite_streaming]