from sensorTemperatura import RetrieveSensorData


class CheckForFire:

    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__retrieveSensorData = RetrieveSensorData(sensor_id)

    def detectFire(self):
        sensor_data = self.__retrieveSensorData.get_data_from_sensor()
        if sensor_data > 500:
            return True
        else:
            return False
