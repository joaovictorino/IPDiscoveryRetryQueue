from queueWrapper import QueueWrapper
from callService import CallService
queueSystem = QueueWrapper()

def callback(body):
    callService = CallService()
    responseTest = callService.call(body.decode())
    queueSystem.publish("response", responseTest)

queueSystem.receive("ip-query", callback, False)
