class Sensor:

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__sensor_data = 0

    def set_sensor_data(self, data):
        self.__sensor_data = data

    def get_sensor_data(self):
        return self.__sensor_data
