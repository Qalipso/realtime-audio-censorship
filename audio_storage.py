from six.moves import queue
class AudioStorage:    
    def __init__(self):
        self.input_audio_stream = []
        self.last_chunk = 0
        self.output_audio_stream = queue.Queue()
        self.audio_wav = []
        self.out_put = []

