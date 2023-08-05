import pika


# Configuração da conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('ENDPOINT RABBITMQ'))
channel = connection.channel()

# Declarar a fila a partir da qual iremos consumir as mensagens
queue_name = 'video-queue'
channel.queue_declare(queue=queue_name, durable=True)

# Função de callback para processar as mensagens recebidas
def callback(ch, method, properties, body):
    # Aqui, você pode processar a mensagem recebida como desejar
    print(f"Recebido: {body}")

# Registrar a função de callback para consumir mensagens
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens. Para sair, pressione CTRL+C')
try:
    # Começar a consumir mensagens indefinidamente
    channel.start_consuming()
except KeyboardInterrupt:
    print('Parando a conexão.')
    connection.close()
