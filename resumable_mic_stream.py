import pyaudio
import time
from six.moves import queue
from constants import STREAMING_LIMIT,SAMPLE_RATE, CHUNK_SIZE
from audio_storage import AudioStorage

class ResumableMicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk_size,inp_device_ind=None):
        self.correct_device = True
        self._rate = rate
        self.chunk_size = chunk_size
        self._num_channels = 1
        self._buff = queue.Queue()
        self.closed = True
        self.start_time = int(round(time.time() * 1000))
        self.restart_counter = 0
        self.audio_input = []
        self.last_audio_input = []
        self.result_end_time = 0
        self.is_final_end_time = 0
        self.final_request_end_time = 0
        self.bridging_offset = 0
        self.new_stream = True
        self._audio_interface = pyaudio.PyAudio()
        try:
            self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=self._num_channels,
            rate=self._rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            input_device_index= inp_device_ind,
            stream_callback=self._fill_buffer,)
        except:
            self.correct_device = False

    def __enter__(self):
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, *args, **kwargs):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        """Stream Audio from microphone to API and to local buffer"""
        while not self.closed:
            data = []

            if self.new_stream and self.last_audio_input:

                chunk_time = STREAMING_LIMIT / len(self.last_audio_input)

                if chunk_time != 0:

                    if self.bridging_offset < 0:
                        self.bridging_offset = 0

                    if self.bridging_offset > self.final_request_end_time:
                        self.bridging_offset = self.final_request_end_time

                    chunks_from_ms = round(
                        (self.final_request_end_time - self.bridging_offset)
                        / chunk_time
                    )

                    self.bridging_offset = round(
                        (len(self.last_audio_input) - chunks_from_ms) * chunk_time
                    )

                    for i in range(chunks_from_ms, len(self.last_audio_input)):
                        data.append(self.last_audio_input[i])

                data.append(self)
                 
                self.new_stream = False

            chunk = self._buff.get()
            self.audio_input.append(chunk)
            if chunk is None:
                return
            audio_stream.audio_wav.append(chunk)  
            audio_stream.input_audio_stream.append(chunk)  
            data.append(chunk)
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                    self.audio_input.append(chunk)
                    audio_stream.audio_wav.append(chunk)
                    audio_stream.input_audio_stream.append(chunk)  
                except queue.Empty:
                    break
        
            yield b"".join(data)

audio_stream = AudioStorage()
mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)