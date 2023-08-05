
# infra-stream-drone

Este é um projeto de infraestrutura que configura dois serviços essenciais para o ambiente de desenvolvimento: Portainer e RabbitMQ. O Portainer é uma plataforma para gerenciar e visualizar contêineres Docker, enquanto o RabbitMQ é um sistema de mensagens para facilitar a comunicação entre os serviços.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o Docker e o Docker Compose na sua máquina. Caso ainda não os tenha instalado, siga as instruções oficiais:

- [Instalação do Docker](https://docs.docker.com/get-docker/)
- [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Subindo a infraestrutura

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu-usuario/infra-stream-drone.git
cd infra-stream-drone
```

2. Agora, vamos subir os serviços utilizando o Docker Compose:

```bash
docker compose up -d
```
Isso iniciará os serviços em segundo plano e você poderá acessar as seguintes interfaces:

- Portainer: [http://localhost:9000](http://localhost:9000)
- RabbitMQ Management: [http://localhost:8081](http://localhost:8081) (usuario/senha: guest/guest)

Para parar os serviços, utilize o seguinte comando:
```bash
docker compose down
```

Se você precisar remover tudo, incluindo os volumes persistentes, utilize o comando:
```bash
docker compose down -v
```
## Subindo o ambiente do n8n

Após configurar a infraestrutura, você pode subir o ambiente do n8n. Siga os passos abaixo:

1. Acesse a pasta `docker/n8n` no diretório do projeto:
```bash
cd docker/n8n
```

2. Execute o comando para subir o serviço do n8n:
```bash
docker compose up -d
```
Isso iniciará o serviço do n8n em segundo plano. O n8n é uma ferramenta de automação que permite criar fluxos de trabalho automatizados usando uma interface gráfica.

Você pode acessar a interface do n8n através do seguinte link: [http://localhost:5678](http://localhost:5678)

## Encerrando o ambiente do n8n

Caso deseje parar o serviço do n8n, utilize o seguinte comando:
```bash
  docker compose down
```
Isso encerrará o serviço do n8n e o ambiente estará desligado.

Lembre-se de que você pode sempre reiniciar os serviços com o comando `docker compose up -d` na pasta correspondente.

Agora você tem uma infraestrutura básica com o Portainer, RabbitMQ e o n8n configurados e prontos para uso. Explore e divirta-se construindo seus projetos!
