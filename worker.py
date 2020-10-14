from queueWrapper import QueueWrapper
from callService import CallService
from logger import Logger

queueSystem = QueueWrapper()

def callback(body):
    callService = CallService()
    loggerNoSQL = Logger()
    responseTest = callService.call(body.decode())
    queueSystem.publish("response", responseTest)
    loggerNoSQL.log(body.decode(), responseTest)

queueSystem.receive("ip-query", callback, False)
