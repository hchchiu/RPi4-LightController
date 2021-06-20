from flask import Flask, render_template, Response
import cv2
import mediapipe
from controlRPi import *

app = Flask(__name__)

#mediapipe hands module
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

#cv2
camera = cv2.VideoCapture(0)
frameWidth = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
fingerCheck=[4,8,12,16,20]
toggle = 1

def gen_frames():  # generate frame by frame from camera
    global toggle
    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
        while True:
            # Capture frame-by-frame
            success, frame = camera.read()  # read the camera frame
            if not success:
                break
            else:
                results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
                handLandmarks_list=[]
                if results.multi_hand_landmarks != None:
                    for handLandmarks in results.multi_hand_landmarks:
                        drawingModule.draw_landmarks(frame, handLandmarks, handsModule.HAND_CONNECTIONS)
                        for point in handsModule.HandLandmark:
                            normalizedLandmark = handLandmarks.landmark[point]
                            pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, frameWidth, frameHeight)
                            handLandmarks_list.append(pixelCoordinatesLandmark)

                ls=[]
                if len(handLandmarks_list) != 0:
                    if handLandmarks_list[8] != None and handLandmarks_list[6] != None:
                        if handLandmarks_list[8][1]> handLandmarks_list[6][1]:
                            ls.append(1)
                            if toggle == 1:
                                turn_off()
                                toggle = 0
                                print('Turn off the light!')
                                #break
                        else:
                            if toggle == 0:
                                turn_on()
                                toggle = 1
                                print('Turn on the light!')
                            ls.append(0)
                #print(ls)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('main.html')

@app.route("/on")
def on():
    global toggle
    turn_on()
    toggle = 1
    return render_template("main.html")

@app.route("/off")
def off():
    global toggle
    turn_off()
    toggle = 0
    return render_template("main.html")

@app.route("/changemode")
def changemode():
    turn_off()
    turn_on()
    return render_template("main.html")

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')