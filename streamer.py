# Streamer v0.0
# Streams video from camera to a local server
# which can be viewed through a web browser
#
# Author: Aashvij Shenai
# Date: 02-Sep-2022

#Imports
import flask
import cv2

###########User inputs###########
# 0 - First camera. If on a laptop, it will be the built-in webcam
camera = 1

#Webserver port
port = 2204
# Displayed on http://<IP>:<port>

#############MAIN#################

#Create Flask object
app = flask.Flask(__name__)

video = cv2.VideoCapture(1)

#Set frame height and width
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def generator(video):
    while True:
        #Read frame from capture
        success, image = video.read()

        #Convert it to a jpeg, then to bytes in order to attach it to HTTP
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Display on the homepage
@app.route('/')
def video_feed():
    global video
    return flask.Response(generator(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)