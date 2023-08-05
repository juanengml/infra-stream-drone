from flask import Flask, render_template, Response
import cv2
from stream import CameraStream, generate_noise_frame, add_timestamp_to_frame
app = Flask(__name__)

# Configurações do RabbitMQ
rabbitmq_host = "endpoint-rabbitmq"
queue_name = 'video-queue-dev'#

camera = CameraStream(rabbitmq_host, queue_name)


def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if success == False:
            frame = generate_noise_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        else:
            frame_buffer = add_timestamp_to_frame(frame)
            yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_buffer + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
