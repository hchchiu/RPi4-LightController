# RPi4LightController

## Introduction
由於每次要睡覺前都在滑手機，滑到一半睡意一來想要可以馬上關燈睡覺，可是卻因為要起身關燈導致睡意又消失，導致每晚的睡覺時間拖到很晚。

基於Raspberry Pi 4 Model B結合[Google Cloud Speech API](https://cloud.google.com/speech-to-text)與[Google Mediapipe](https://google.github.io/mediapipe/)做到語音辨識以及手勢辨識開關燈。

## Build
下載需要的檔案以及packages
```shell
#download files
$ git clone https://github.com/hchchiu/RPi4LightController.git

#change directory
$ cd RPi4LightController

#install packages
$ pip3 install -p requirments.txt
```
透過[Google API Console](https://console.developers.google.com/)申請Google Cloud Speech API金鑰，並且將金鑰檔案(JSON File)設定到環境變數中
```shell
$ export GOOGLE_APPLICATION_CREDENTIALS="GOOGLE-CLOUD-SPEECH-API_KEY PATH"
```
## Details

## Results

## References
