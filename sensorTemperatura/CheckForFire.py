from sensorTemperatura import RetrieveSensorData


class CheckForFire:

    __sensor_id = 0
    __receivedSensorData = 0
    __retrieveSensorData = -1

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__retrieveSensorData = RetrieveSensorData(sensor_id)

    def detectFire(self):
        self.__retrieveSensorData.get_data_from_sensor()




