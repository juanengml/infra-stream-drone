import cv2
import requests
import base64

endpoint = "endpoint-n8n"  # Substitua pelo endpoint da sua API
video_stream = "http://142.0.109.159/mjpg/video.mjpg"  # URL do stream de vídeo

def main():
    cap = cv2.VideoCapture(video_stream)
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Converte a imagem em formato de bytes usando a extensão .jpg
        _, img_encoded = cv2.imencode('.jpg', frame)

        # Codifica a imagem em Base64
        img_base64 = base64.b64encode(img_encoded).decode()

        # Prepara os dados para enviar na requisição
        body = {
            'data': img_base64
        }

        # Faz a requisição HTTP POST para enviar o quadro (imagem) para a API
        response = requests.post(endpoint, json=body)

        # Verifica se a requisição foi bem-sucedida e exibe o status da resposta
        if response.status_code == 200:
            print(count, "Quadro enviado com sucesso.")
        else:
            print("Falha ao enviar o quadro. Código de status:", response.status_code)
        count = count + 1
    cap.release()

if __name__ == "__main__":
    main()
