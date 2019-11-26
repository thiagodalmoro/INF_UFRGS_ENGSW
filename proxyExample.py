import publishSubscribe

#exemplo de como usar a classe Proxy
#apenas inicializa um Proxy entre as portas 5556 e 5555

proxyInstance = publishSubscribe.Proxy(5556, 5555)
proxyInstance.start()