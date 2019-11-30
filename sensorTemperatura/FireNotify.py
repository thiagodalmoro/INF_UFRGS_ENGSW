import publishSubscribe
from sensorTemperatura import CheckForFire


class FireNotify:

    __is_there_fire = False

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__check_for_fire = CheckForFire(sensor_id)
        self.__publisherInstance = publishSubscribe.Publisher(5556)

    def __send_fire_notification(self):
        self.__publisherInstance.publish(b"This is the message")

    def check_for_fire(self):
        return False

