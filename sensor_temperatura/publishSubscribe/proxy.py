import time
import zmq
import sys
from threading import Thread

#Esta classe abstrai um proxy de uma arquitetura publish-subscribe estendida
#Quando um objeto desta classe é criado, ele inicializa os sockets do proxy. Para rodar o proxy, é necessário chamar o método start(), já que ele roda em uma thread separada
#Recebe mensagens de Publishers no socket da porta receiverPort e repassa estas mensagens para Subscribers no socket da porta senderPort
class Proxy(Thread):

    receiverSocket = 0
    senderSocket = 0

    #construtor, inicializa os sockets para receber e enviar mensagens nas portas receiverPort e senderPort, respectivamente
    def __init__(self, receiverPort, senderPort):

        context = zmq.Context()
    
        self.receiverSocket = context.socket(zmq.SUB)        #cria um socket do tipo SUB para ouvir mensagens na porta receiverPort
        self.receiverSocket.bind("tcp://*:%d" % receiverPort)
        self.receiverSocket.setsockopt(zmq.SUBSCRIBE, b'')   #subscribe para receber qualquer mensagem

        self.senderSocket = context.socket(zmq.PUB)          #cria um socket do tipo PUB para enviar mensagens na porta senderPort
        self.senderSocket.bind("tcp://*:%d" % senderPort)

        Thread.__init__(self)


    def run(self):
        zmq.proxy(self.receiverSocket, self.senderSocket)