from queueWrapper import QueueWrapper

def decodeOption(optionNumber):
    if int(optionNumber) == 1:
        return "ip"
    elif int(optionNumber) == 2:
        return "city"
    elif int(optionNumber) == 3:
        return "loc"
    elif int(optionNumber) == 4:
        return "country"

def showResult(message):
    print(message.decode())

print("1. ip")
print("2. cidade")
print("3. localização")
print("4. pais")

optionNumber = input("O que você deseja saber? (escolha pelo número) ")

option = decodeOption(optionNumber)

queueSystem = QueueWrapper()

queueSystem.publish("ip-query", option)

queueSystem.receive("response", showResult, True)