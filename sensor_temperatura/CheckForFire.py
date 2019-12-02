from RetrieveSensorData import *

class CheckForFire:
    sensorData:RetrieveSensorData

    def __init__(self):
        self.sensorData = RetrieveSensorData()

    def detectFire(self):
        if(self.sensorData.getDataFromSensor() >= 50): return True
        else: return False

    def simulate_toggleFire(self):
        self.sensorData.simulate_toggleFire()
