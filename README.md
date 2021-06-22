# RPi4 LightController

## Introduction
由於每次要睡覺前都在滑手機，滑到一半睡意一來想要可以馬上關燈睡覺，可是電燈的開關在遠處，而起身關燈導致睡意又消失，因此每晚的睡覺時間都會拖到很晚。

因此本專題是將Raspberry Pi 4 Model B結合[Google Cloud Speech API](https://cloud.google.com/speech-to-text)與[Google MediaPipe](https://google.github.io/mediapipe/)模擬智慧開關，做到以下三種方法開燈:
- 聲音辨識開關燈
- 手勢辨識開關燈
- 網頁按鈕開關燈

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
- Python == 3.7

## Supported Platform
* Raspberry PI 4 - Raspbian Buster

## Build

在樹梅派中建立虛擬環境(Optional)
```bash
#install virtualenv package
$ sudo pip3 install virtualenv

#create virtual env
$ sudo virtualenv <YOUR ENV NAME>

#變更目錄權限為pi
$ sudo chown -R pi:pi <YOUR ENV NAME>

#檢查目錄權限是否為pi
$ ls -al
```

進入及退出虛擬環境指令
```bash
#進入虛擬環境
$ source <YOUR ENV NAME>/bin/activate

#退出虛擬環境
$ deactivate
```

### Installation
下載需要的檔案以及packages
```bash
#download files
$ git clone https://github.com/hchchiu/RPi4-LightController.git

#change directory
$ cd RPi4-LightController
```
根據環境擇一指令
```bash
#在虛擬環境中
$ pip3 install -r requirement.txt

#不在虛擬環境中
$ sudo pip3 install -r requirement.txt
```

透過[Google API Console](https://console.developers.google.com/)或是[Google Cloud Speech-To-Text Doc](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)申請Google Cloud Speech API金鑰，並且將金鑰檔案(JSON File)路徑設定到環境變數中
```bash
#set your api key path to the environment variable
$ export GOOGLE_APPLICATION_CREDENTIALS="<YOUR-GOOGLE-CLOUD-SPEECH-API_KEY_PATH>"
```

### Hardware
#### Pre-requisites
1. Raspberry Pi 4 Model B
2. Webcam(含麥克風功能)
3. Servo MG996R or SG90

#### 安裝
* Servo與樹梅派連接的腳位
  - VDD(pin 2)
  - Ground(pin 6)
  - PWM(pin 12)
* Webcam透過USB連接到樹梅派
* 將Servo安裝於電燈的按鈕上

<div>
<img src="/doc/pinout.png" width=80%>
</div>

## Usage
- 輸入以下指令開始執行。
```bash
#start detect
$ python3 start.py
```

- 查看ip位置以及port(以這裡為例:192.168.0.104:5000)。
<div>
<img src="/doc/ip.jpg" width=70%>
</div>

- 在相同網域底下輸入剛才查看的ip位置及port(以這裡為例:192.168.0.104:5000)，即可透過網頁呈現。
- 此時使用者可以透過手勢、聲音或網頁控制電燈的開關。
* 手勢控制
  - **手掌開** &rArr; 開燈
  - **手掌關** &rArr; 關燈
* 聲音控制
  - 說出 **"開啟電燈"** &rArr; 開燈
  - 說出 **"關閉電燈"** &rArr; 關燈
* 網頁控制
  - 按下 **Turn On** &rArr; 開燈
  - 按下 **Turn Off** &rArr; 關燈
  - 按下 **Change Mode** &rArr; 改變電燈模式(依照每個人的電燈功能而有所不同)
<div>
<img src="/doc/webui.png" width=70%>
</div>

## Details
* 透過三種輸入判斷使用者要開燈還是關燈:

### 聲音辨識
1. 聲音輸入
2. 藉由Pyaudio將使用者說出的音訊轉成音檔
3. 藉由Google Cloud API將音檔中的音訊轉為文字(Speech to text)
4. 判斷使用者說出的文字
5. 控制伺服馬達開關電燈

### 手勢辨識
1. 手勢輸入
2. 藉由Google MediaPipe辨識手指的位置
3. 藉由手指位置判斷手掌開合
4. 控制伺服馬達開關電燈

### 網頁控制及顯示
1. 用Flask將樹梅派當作server
2. 將Webcam拍攝的影像傳送到網頁中
3. 按下動作按鈕
4. 控制伺服馬達開關電燈

<div>
<img src="/doc/RPi4LightController2.svg" width=80%>
</div>

## Results
### 手勢辨識開關燈
<div>
<img src="/doc/IMG_6110_2.gif" width=40%>
</div>

### 網頁控制開關燈
<div>
<img src="/doc/webtn2.gif" width=55%>
</div>

### 聲音辨識開關燈(點擊圖片)
<div>
<a href="https://youtu.be/hZ0RpbavAHg" target="_blank"><img src="/doc/thumbnail.jpg" 
alt="聲音辨識開燈" width=55% />
</a>
</div>


## References

- [Google Cloud Speech API](https://cloud.google.com/speech-to-text)
- [Google Mediapipe](https://google.github.io/mediapipe/)
- [Google Cloud Speech API Documentation](https://github.com/googleapis/python-speech)
- [MediaPipe tutorial](https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/)
- [在樹莓派建立Python虛擬環境](https://dsalearning.github.io/aiot/raspberry-pip3-create-env/)
- [Pyaudio 教學](https://zwindr.blogspot.com/2017/03/python-pyaudio.html)
