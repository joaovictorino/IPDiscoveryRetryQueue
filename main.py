import pika

print("1. ip")
print("2. cidade")
print("3. localização")
print("4. pais")

opcao = input("O que você deseja saber? (escolha pelo número) ")

if int(opcao) == 1:
    opcao = "ip"
elif int(opcao) == 2:
    opcao = "city"
elif int(opcao) == 3:
    opcao = "loc"
else:
    opcao = "country"

params = pika.URLParameters("amqps://kisseibz:A-TH1pbRRQ_yXvmPnh2Xl8X6MhsKTeBp@chimpanzee.rmq.cloudamqp.com/kisseibz")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='ip-query')

channel.basic_publish(exchange="", routing_key="ip-query", body=opcao)

channel.queue_declare(queue='response')

def callback(channel, method, properties, body):
    print(body.decode())
    channel.stop_consuming()

channel.basic_consume(
    queue='response', on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()