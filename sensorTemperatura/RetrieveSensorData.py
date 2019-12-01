from simulation.Sensor import Sensor


class RetrieveSensorData:

    def __init__(self, sensorID):
        self.__sensorID = sensorID
        self.__sensor = Sensor(sensorID, "temp")

    def getDataFromSensor(self):
        return self.__sensor.getSensorData()
