from simulation.Sensor import Sensor


class RetrieveSensorData:

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__sensor = Sensor(sensor_id)

    def get_data_from_sensor(self):
        return self.__sensor.get_sensor_data()
