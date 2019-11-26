import publishSubscribe
import time

#exemplo de como usar a classe Publisher
#um Publisher que fica a cada 2 segundos enviando mensagens com prefixo prefix1 para a porta 5556

publisherInstance = publishSubscribe.Publisher(5556)

while True:
    publisherInstance.publish(b"prefix1 aaaaaaaaaaaaaaaaaaaaaaTESTE")
    time.sleep(2)