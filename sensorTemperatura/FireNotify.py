import publishSubscribe
import time
from sensorTemperatura import CheckForFire


class FireNotify:
    __is_there_fire = False
    __keep_checking = True

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__check_for_fire = CheckForFire(sensor_id)
        self.__publisherInstance = publishSubscribe.Publisher(5556)
        self.check_for_fire()

    def __send_fire_notification(self):
        self.__publisherInstance.publish(b"fire_notification sensor_id: %ds" % self.__sensor_id)

    def check_for_fire(self):
        while self.__keep_checking:
            __is_there_fire = self.__check_for_fire.detectFire()
            if __is_there_fire:
                self.__send_fire_notification()
            time.sleep(1)
