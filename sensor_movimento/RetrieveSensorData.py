class RetrieveSensorData:
    sensorData = 0
    isIntruder = False

    def __init__(self):
        self.sensorData = 0

    def getDataFromSensor(self):
        return self.sensorData

    def simulate_toggleIntruder(self):
        if not(self.isIntruder):
            self.sensorData = 50
            self.isIntruder = True
        else :
            self.sensorData = 0
            self.isIntruder = 0
