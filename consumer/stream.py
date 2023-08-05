import cv2
import pika
import base64
from io import BytesIO
import numpy as np


class CameraStream(object):
    def __init__(self, rabbitmq_host, queue_name):
        self.rabbitmq_host = rabbitmq_host
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)

    def __formatter(self, message):
        # Decode base64 and convert to OpenCV frame
        binary_image = base64.b64decode(message)
        frame = cv2.imdecode(np.frombuffer(binary_image, dtype=np.uint8), cv2.IMREAD_COLOR)
        return frame

    def read(self):
        method_frame, properties, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
        print(method_frame, properties, body)
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
