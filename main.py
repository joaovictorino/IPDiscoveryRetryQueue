from queueWrapper import QueueWrapper

def decodificarOpcao(opcaoNumero):
    if int(opcaoNumero) == 1:
        return "ip"
    elif int(opcaoNumero) == 2:
        return "city"
    elif int(opcaoNumero) == 3:
        return "loc"
    elif int(opcaoNumero) == 4:
        return "country"

def exibirResultado(message):
    print(message.decode())

print("1. ip")
print("2. cidade")
print("3. localização")
print("4. pais")

opcaoNumero = input("O que você deseja saber? (escolha pelo número) ")

opcao = decodificarOpcao(opcaoNumero)

queueSystem = QueueWrapper()

queueSystem.publish("ip-query", opcao)

queueSystem.receive("response", exibirResultado, True)