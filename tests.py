# -*- encoding: utf-8 -*-

import unittest
from audio_storage import AudioStorage
from filter_vocabulary import FilterVocabulary
from resumable_mic_stream import mic_manager
from google.cloud import speech
import os

class TestAudioStorage(unittest.TestCase):
    def setUp(self):
        self.storage = AudioStorage()
        self.storage.input_audio_stream.append([ x for x in range(100)])
        self.storage.output_audio_stream.put(b"21334")

    def test_queue(self):
        self.assertEqual(self.storage.output_audio_stream.get(), b'21334')
        self.assertTrue(self.storage.output_audio_stream.empty())
    
    def test_list(self):
        self.assertTrue(len(self.storage.input_audio_stream) == 1)
        self.assertFalse(len(self.storage.input_audio_stream[0]) != 100)
        self.storage.input_audio_stream = []
        self.assertEqual(self.storage.input_audio_stream, [])
        self.storage.input_audio_stream.append(21)
        self.assertEqual(self.storage.input_audio_stream[0], 21)




class TestFilterVocabulary(unittest.TestCase):
    def setUp(self):
        self.filepath = os.path
    def test_create(self):
        voc = FilterVocabulary()
        self.assertEqual(voc.create(), None)
        self.assertTrue(voc.create("dsfsdf"),"Возникли ошибки при попытке открыть файл")

    def test_single_letter(self):
        voc = FilterVocabulary()
        voc.create(self.filepath.join('./tests_data/single_letter.txt'))
        self.assertEqual(len(voc.vocabulary), 14)

    def test_eng_in_rus(self):
        voc = FilterVocabulary()
        self.assertIn("английского",voc.create(self.filepath.join('./tests_data/english_letter_in_rus.txt')))
    
    def test_multilines(self):
        voc = FilterVocabulary()
        voc.create(self.filepath.join('./tests_data/multilines.txt'))
        self.assertEqual(9,len(voc.vocabulary))

    def test_uppercase(self):
        voc = FilterVocabulary()
        voc.create(self.filepath.join('./tests_data/uppercase.txt'))
        self.assertEqual(7,len(voc.vocabulary))
    
    def test_wrong_separator(self):
        voc = FilterVocabulary()
        voc.create(self.filepath.join('./tests_data/wrong_separator.txt'))
        self.assertEqual(5,len(voc.vocabulary))
               
class TestMicrophoneStream(unittest.TestCase):
    
    def test_input_stream(self):
        with mic_manager as stream:
            # self.assertFalse(mic_manager.closed)    
            for i in range(100):
                audio_generator = stream.generator()
                requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator)
                self.assertFalse(str(audio_generator)  == "") 
       
    
    def test_free_memory(self):
        with mic_manager as stream:
            for i in range(10):
                audio_generator = stream.generator()
                i = audio_generator
        self.assertTrue(mic_manager.closed) 
        


if __name__ == '__main__':
    unittest.main()