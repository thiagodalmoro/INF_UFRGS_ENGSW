import zmq
import sys

#Esta classe abstrai um subscriber de uma arquitetura publish-subscribe
#Recebe mensagens com os prefixos presentes na lista prefixesList num socket na porta port e as passa como parâmetros para a função messageReceived (que pode ser sobrescrita por uma classe filha) 
class Subscriber:

    #socket no qual este subscriber vai esperar por mensagens
    socket = -1

    #Inicializa o socket deste subscriber
    def socketInit(self, prefixesList, port):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)                       #cria socket do tipo SUB para receber atualizações
        self.socket.connect("tcp://localhost:%d" % port)
        for prefix in prefixesList:
            self.socket.setsockopt_string(zmq.SUBSCRIBE, prefix)    #configura todos os prefixos para os quais este subscriber estará subscribed


    #função chamada quando uma nova mensagem é recebida. Deve ser sobrescrita por classes que herdem desta
    def messageReceived(self, message):
        print("recebi uma mensagem!")
        print(message)


    #bloqueia esperando por uma nova mensagem e, quando essa mensagem chegar, chama a função messageReceived
    def waitForMessage(self):
        newMessage = self.socket.recv()
        self.messageReceived(newMessage)