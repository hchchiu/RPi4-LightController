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
|ffmpeg|
|opencv|

## Supported Python Version
Python == 3.7

## Build

在樹梅派中建立虛擬環境(Optional)
```bash
#install virtualenv package
$ sudo pip3 install virtualenv

#create virtual env
$ sudo virtualenv "<YOUR ENV NAME>"

#變更目錄權限為pi
$ sudo chown -R pi:pi "<YOUR ENV NAME>"
```

### Installation
下載需要的檔案以及packages
```bash
#download files
$ git clone https://github.com/hchchiu/RPi4-LightController.git

#change directory
$ cd RPi4-LightController

#install all packages
$ sudp pip3 install -r requirments.txt
```

透過[Google API Console](https://console.developers.google.com/)申請Google Cloud Speech API金鑰，並且將金鑰檔案(JSON File)設定到環境變數中
```bash
#set your api key path to the environment variable
$ export GOOGLE_APPLICATION_CREDENTIALS="<YOUR-GOOGLE-CLOUD-SPEECH-API_KEY_PATH>"
```

### Hardware
#### Pre-requisites
1. Raspberry Pi 4 Model B
2. Webcam
3. Servo MG996R or SG90

#### 安裝
* Servo與樹梅派連接的腳位
  - VDD(pin 2)
  - Ground(pin 6)
  - PWM(pin 12)
* Webcam透過USB連接到樹梅派
* 將Servo安裝於電燈的按鈕上

<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/doc/pinout.png" width=80%>
</div>

## Usage
- 輸入以下指令開始執行。
```bash
#start all the program
$ python3 start.py
```

- 查看ip位置以及port(以這裡為例:192.168.0.104:5000)。
<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/doc/ip.jpg" width=60%>
</div>

- 在相同網域底下輸入剛才查看的ip位置及port(192.168.0.104:5000)，即可透過網頁呈現。
- 此時使用者可以透過手勢或聲音控制電燈的開關。
* 手勢控制
  - **手掌開** &rArr; 開燈
  - **手掌關** &rArr; 關燈
* 聲音控制
  - 說出 **"開啟電燈"** &rArr; 開燈
  - 說出 **"關閉電燈"** &rArr; 關燈
<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/doc/webui.png" width=60%>
</div>

## Details
1. 透過兩種輸入判斷使用者要開燈還是關燈，分別是
  - 聲音輸入
  - 手勢輸入
2. 使用者說出
<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/doc/RPi4LightController.svg" width=80%>
</div>

## Results & Demo
- 手勢辨識開關燈
<div>
<img src="https://github.com/hchchiu/RPi4-LightController/blob/master/doc/IMG_6110_2.gif" width=35%>
</div>


- 聲音辨識開關燈
https://youtu.be/hZ0RpbavAHg

## References

- [Google Cloud Speech API](https://cloud.google.com/speech-to-text)
- [Google Mediapipe](https://google.github.io/mediapipe/)
- [Google Cloud Speech Documentation](https://github.com/googleapis/python-speech)
- [MediaPipe tutorial](https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/)
