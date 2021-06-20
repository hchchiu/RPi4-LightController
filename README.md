# RPi4 LightController

## Introduction
由於每次要睡覺前都在滑手機，滑到一半睡意一來想要可以馬上關燈睡覺，可是卻因為要起身關燈導致睡意又消失，導致每晚的睡覺時間拖到很晚。

基於Raspberry Pi 4 Model B結合[Google Cloud Speech API](https://cloud.google.com/speech-to-text)與[Google Mediapipe](https://google.github.io/mediapipe/)做到語音辨識以及手勢辨識開關燈。

## Dependencies
|Name|
|----|
|numpy|
|Flask|
|scipy|
|pyaudio|
|mediapipe-rpi4|
|google-cloud-speech|
|RPI.GPIO|
|ffmpeg|
|opencv-python==4.4.0.44|


## Build

### Supported Python Version
Python == 3.7

### Installation
下載需要的檔案以及packages
```bash
#download files
$ git clone https://github.com/hchchiu/RPi4-LightController.git

#change directory
$ cd RPi4-LightController

#install packages
$ pip3 install -r requirments.txt
```

透過[Google API Console](https://console.developers.google.com/)申請Google Cloud Speech API金鑰，並且將金鑰檔案(JSON File)設定到環境變數中
```bash
#set your api key path to the environment variable
$ export GOOGLE_APPLICATION_CREDENTIALS="GOOGLE-CLOUD-SPEECH-API_KEY_PATH"
```

### Hardware
- Webcam
- Servo MG996R or SG90
- Raspberry Pi 4 Model B

<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/pinout.png" width=80%>
</div>


## Details

## Results

## References
