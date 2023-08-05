import cv2, pendulum
import pika
import base64
from io import BytesIO
import numpy as np


def bytes_to_opencv_image(byte_data):
    # Transforma os bytes em uma matriz NumPy
    nparr = np.frombuffer(byte_data, np.uint8)
    
    # Decodifica a imagem usando o OpenCV
    img_opencv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Se a imagem for em escala de cinza, use cv2.IMREAD_GRAYSCALE em vez de cv2.IMREAD_COLOR.

    return img_opencv

class CameraStream(object):
    def __init__(self, rabbitmq_host, queue_name):
        self.rabbitmq_host = rabbitmq_host
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)

    def __formatter(self, message):
        binary_image = base64.b64decode(message)
        frame = bytes_to_opencv_image(binary_image)
        return frame

    def read(self):
        method_frame, properties, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
        if method_frame is not None:
            frame = self.__formatter(body)
            return True, frame
        else:
            return False, None


def generate_noise_frame():
    # Gerar um quadro de vídeo aleatório (ruído)
    VIDEO_WIDTH = 640
    VIDEO_HEIGHT = 480
    VIDEO_FPS = 30
    frame = np.random.randint(0, 256, (VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
    
    # Adicionar a mensagem "Sem Sinal" no centro da imagem
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Sem Sinal'
    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = (VIDEO_WIDTH - textsize[0]) // 2
    text_y = (VIDEO_HEIGHT + textsize[1]) // 2
    cv2.putText(frame, text, (text_x, text_y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    return cv2.imencode('.jpg', frame)[1].tobytes()




def add_timestamp_to_frame(frame):
    # Obtem a data e hora atual usando Pendulum
    current_datetime = pendulum.now(tz='America/Sao_Paulo').to_datetime_string()


    # Adiciona o carimbo de data e hora ao quadro
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottom_left_corner = (10, 60)
    font_scale = 1
    font_color = (255, 255, 255)  # Branco (RGB)
    line_type = 2

    cv2.putText(frame, current_datetime, bottom_left_corner, font, font_scale, font_color, line_type)

    # Converte o quadro modificado em formato de buffer
    _, buffer = cv2.imencode('.jpg', frame)
    frame_buffer = buffer.tobytes()

    return frame_buffer
