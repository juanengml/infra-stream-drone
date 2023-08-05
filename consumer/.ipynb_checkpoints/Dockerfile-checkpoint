# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY app.py .
COPY stream.py .

# Instala as dependências do aplicativo
RUN pip install Flask opencv-python

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Comando para rodar o aplicativo quando o container for iniciado
CMD ["python", "app.py"]
