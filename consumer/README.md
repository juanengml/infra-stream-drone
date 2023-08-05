# Flask Video Streaming com RabbitMQ

Este projeto é um exemplo de streaming de vídeo utilizando o Flask para servir o vídeo em tempo real e o RabbitMQ como intermediário para a transmissão dos frames de vídeo.

## Configuração

Certifique-se de ter o Python instalado em sua máquina.

Instale as dependências necessárias executando o seguinte comando:


``` bash
pip install Flask opencv-python
```

Além disso, você precisará configurar o RabbitMQ para que o aplicativo de streaming de vídeo possa enviar os frames para a fila correta. Substitua `ENDPOINT RABBITQ` no arquivo `app.py` com o endereço do seu servidor RabbitMQ.

## Executando o Aplicativo

Para iniciar o servidor de streaming de vídeo, execute o seguinte comando na raiz do projeto:

``` bash
python app.py
```


O servidor será iniciado e estará ouvindo em `http://localhost:5000/`. Você poderá acessar o vídeo em tempo real em `http://localhost:5000/video_feed`.

## Entendendo o Código

O aplicativo utiliza o Flask para criar um servidor web simples que disponibiliza uma rota `/video_feed` para transmitir o vídeo. A transmissão de vídeo é feita através da função `gen_frames()` que captura os frames da câmera ou gera um frame de ruído quando não há sucesso na captura. Os frames são enviados em formato de imagem JPEG e são transmitidos em sequência usando o cabeçalho `multipart/x-mixed-replace`.

A classe `CameraStream` é responsável por ler os frames da câmera e enviá-los para a fila no RabbitMQ. Caso a captura da câmera falhe, é gerado um frame de ruído usando a função `generate_noise_frame()`.

## Rotas

- `/` : Página inicial que renderiza o template `index.html`.
- `/video_feed` : Rota de streaming de vídeo que retorna os frames em tempo real.

## Recursos Adicionais

O aplicativo acompanha um template HTML básico `index.html`, que pode ser personalizado para exibir o vídeo em uma página da web.

## Notas

- Este é um exemplo básico e não foi otimizado para cenários de produção.
- Certifique-se de ter a biblioteca OpenCV instalada corretamente para a captura de vídeo funcionar adequadamente.

Agora você tem um servidor de streaming de vídeo utilizando Flask e RabbitMQ. Explore o código e faça melhorias conforme necessário para atender aos requisitos do seu projeto. Divirta-se criando aplicações de streaming interativas!
