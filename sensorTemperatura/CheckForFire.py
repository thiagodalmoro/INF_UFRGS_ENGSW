from sensorTemperatura import RetrieveSensorData


class CheckForFire:

    def __init__(self, sensorID):
        self.__sensorID = sensorID
        self.__retrieveSensorData = RetrieveSensorData(sensorID)

    def detectFire(self):
        sensorData = self.__retrieveSensorData.getDataFromSensor()
        if sensorData > 500:
            return True
        else:
            return False
