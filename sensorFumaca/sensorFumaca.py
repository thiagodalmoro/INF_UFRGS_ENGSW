import time
import sys
import publishSubscribe
import zmq


#Esta classe abstrai um socket PUB do pacote zeroMQ e espera uma arquitetura publish-subscribe estendida com um proxy
class sensorFumaca:

    #referência ao socket deste publisher
    # socket = -1

    #construtor da classe, apenas inicializa o socket
    def __init__(self, proxyPort):
        self.socketInit(proxyPort)


    #Inicializa o socket deste publisher, dada a porta onde estará o proxy (ver classe Proxy em ./proxy.py)
    def socketInit(self, proxyPort):
        context = zmq.Context()                                 #referencia ao contexto atual, necessária pra criar um novo socket
        self.socket = context.socket(zmq.PUB)                   #criação de um socket do tipo PUB (pois ele será quem publica as atualizações)
        self.socket.connect("tcp://localhost:%d" % proxyPort)   #conecta este socket ao proxy (ver classe Proxy em ./proxy.py)


    #publica a mensagem message no socket deste publisher
    def publish(self, message):
        self.socket.send(b"%s" % message)


