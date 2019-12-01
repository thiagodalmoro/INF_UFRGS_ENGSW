import publishSubscribe
import time
from sensorTemperatura import CheckForFire


class FireNotify:
    __is_there_fire = False
    __keep_checking = True

    def __init__(self, sensorID):
        self.__sensorID = sensorID
        self.__checkForFire = CheckForFire(sensorID)
        self.__publisherInstance = publishSubscribe.Publisher(5556)
        self.checkForFire()

    def __sendFireNotification(self):
        self.__publisherInstance.publish(b"fire_notification sensor_id: %ds" % self.__sensorID)

    def checkForFire(self):
        while self.__keep_checking:
            __is_there_fire = self.__checkForFire.detectFire()
            if __is_there_fire:
                self.__sendFireNotification()
            time.sleep(1)
