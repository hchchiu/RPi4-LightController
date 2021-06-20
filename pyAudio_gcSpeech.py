from google.cloud import speech
from scipy import fftpack
from controlRPi import *

import pyaudio
import numpy as np
import wave
import time
import os
import io


print('*Connect to the google!')
client = speech.SpeechClient()

def speech2Text():
    print('*Start Google speech API!')
    with io.open('out.mp3', "rb") as audio_file:
        content = audio_file.read()
        mtime = time.ctime(os.path.getmtime('./out.mp3'))
    print(mtime)

    #audio = speech.RecognitionAudio(uri=gcs_uri)
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="zh-TW",
    )

    # Detects speech in the audio file
    print('Wait for Response!')
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print('You say:',result.alternatives[0].transcript)
        if result.alternatives[0].transcript == '開啟電燈':
            print('Start turn on the light!')
            turn_on()
            
        elif result.alternatives[0].transcript == '關閉電燈':
            print('Start turn off the light!')
            turn_off()


def recording(filename, time=0, threshold=6000):

    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 
    CHANNELS = 1  
    RATE = 16000  
    RECORD_SECONDS = time  
    WAVE_OUTPUT_FILENAME = filename 
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("* START Recording...")
    frames = []
    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        stopflag = 0
        stopflag2 = 0
        start=0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))

            fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            if sum(fft_data) // len(fft_data) > threshold:
                frames.append(data)
                start=1
                #print("This is in if")
            else:
                #print("This is in else")
                if start == 1:
                    frames.append(data)
                    frames.append(data)
                    frames.append(data)
                    break

                continue
    print("* END Recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    speech2Text()


print("Execute web_app.py")
os.system("python3 web_app.py &")
while True:
    recording('out.mp3') 