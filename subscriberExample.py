import publishSubscribe

#exemplo de uso da classe Subscriber
#cria uma classe concreta chamada MySubscriber que herda da classe abstrata Subscriber e sobrescreve a função messageReceived
#espera receber 5 mensagens com prefixo prefix1, prefix2 ou prefix3 e então termina

class MySubscriber(publishSubscribe.Subscriber):

    def __init__(self, prefixesList, port):
        self.socketInit(prefixesList, port)
        print("Subscriber waiting at port %d" % port)
        numMsgs = 0
        while numMsgs < 5:
            self.waitForMessage()
            numMsgs = numMsgs + 1

    def messageReceived(self, message):
        print("I received a message hell yeah")
        print("message: %s" % message)

subscriberInstance = MySubscriber(["prefix1", "prefix2", "prefix3"], 5555)