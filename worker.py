from queue import Queue
from requestServiceIP import call

queueSystem = Queue()

def callback(body):
    responseTest = call(body.decode())
    queueSystem.publish("response", responseTest)

queueSystem.receive("ip-query", callback, False)
