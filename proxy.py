import publishSubscribe

proxyInstance = publishSubscribe.Proxy(5556, 5555)
proxyInstance.start()

proxyInstance2 = publishSubscribe.Proxy(5557, 5558)
proxyInstance2.start()