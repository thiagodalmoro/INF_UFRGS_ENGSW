from RetrieveSensorData import *

class CheckForIntruder:
    sensorData:RetrieveSensorData
    isAlertModeActive = False

    def __init__(self):
        self.sensorData = RetrieveSensorData()

    def detectIntruder(self):
        if(self.sensorData.getDataFromSensor() >= 50 and self.isAlertModeActive): 
            return True
        else: return False

    def setAlertMode(self, isActive):
        self.isAlertModeActive = isActive

    def simulate_toggleIntruder(self):
        self.sensorData.simulate_toggleIntruder()
