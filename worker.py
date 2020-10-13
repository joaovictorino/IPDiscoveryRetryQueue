import pika
from requestServiceIP import RequestServiceIP

params = pika.URLParameters("amqps://kisseibz:A-TH1pbRRQ_yXvmPnh2Xl8X6MhsKTeBp@chimpanzee.rmq.cloudamqp.com/kisseibz")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='ip-query')
channel.queue_declare(queue='response')

def callback(ch, method, properties, body):
    request = RequestServiceIP()
    response = request.call(body.decode())
    channel.basic_publish(exchange="", routing_key="response", body=response)

channel.basic_consume(
    queue='ip-query', on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()