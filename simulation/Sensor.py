import multiprocessing
import os
import threading
import time

from publishSubscribe import Subscriber


class Sensor(Subscriber):

    def __init__(self, sensor_id, prefix):
        self.__sensor_id = sensor_id
        self.__sensor_data = 0
        self.socketInit(prefix, 5555)
        while True:
            self.waitForMessage()

    def messageReceived(self, message):
        # state_type, data = message.split(":")
        # self.__sensor_data = data
        # print(state_type)
        # print(data)
        print(self.__sensor_id)

    def get_sensor_data(self):
        return self.__sensor_data
