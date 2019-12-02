from RetrieveSensorData import *

class CheckForBadWeather:
    sensorData:RetrieveSensorData

    def __init__(self):
        self.sensorData = RetrieveSensorData()

    def detectBadWeather(self):
        if(self.sensorData.getDataFromSensor() >= 50): return True
        else: return False

    def simulate_toggleBadWeather(self):
        self.sensorData.simulate_toggleBadWeather()
