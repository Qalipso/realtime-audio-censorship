from google.cloud import speech
STREAMING_LIMIT = 300000  # 5 minutes
SAMPLE_RATE = 16000
CHUNK_SIZE = int(SAMPLE_RATE / 10)  #100ms
config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code="ru-RU",
        max_alternatives=1,
        enable_word_time_offsets= True 
    )

STREAMING_CONFIG = speech.StreamingRecognitionConfig(
config=config, interim_results=True
)