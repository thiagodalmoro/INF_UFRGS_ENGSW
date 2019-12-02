class RetrieveSensorData:
    sensorData = 0
    isBadWeather = False

    def __init__(self):
        self.sensorData = 0

    def getDataFromSensor(self):
        return self.sensorData

    def simulate_toggleBadWeather(self):
        if not(self.isBadWeather):
            self.sensorData = 50
            self.isBadWeather = True
        else :
            self.sensorData = 0
            self.isBadWeather = 0
