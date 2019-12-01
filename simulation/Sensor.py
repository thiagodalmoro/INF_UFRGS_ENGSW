from publishSubscribe import Subscriber


class Sensor(Subscriber):

    def __init__(self, sensorID, prefix):
        self.__sensorID = sensorID
        self.__sensorData = 0
        self.socketInit(prefix, 5555)
        while True:
            self.waitForMessage()

    def messageReceived(self, message):
        state_type, data = message.decode("utf-8").split(":")
        self.__sensorData = data
        print(data)

    def getSensorData(self):
        return self.__sensorData
