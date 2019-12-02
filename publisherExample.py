import publishSubscribe
import time

#exemplo de como usar a classe Publisher
#um Publisher que fica a cada 2 segundos enviando mensagens com prefixo prefix1 para a porta 5556

publisherInstance = publishSubscribe.Publisher(5557)

while True:
    publisherInstance.publish(b"[SmartlockConfig] 1")
    print("TRANCOU")
    time.sleep(3)
    publisherInstance.publish(b"[SmartlockConfig] 0")
    print("DESTRANCOU")
    time.sleep(3)
    