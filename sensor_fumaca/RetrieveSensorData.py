class RetrieveSensorData:
    sensorData = 0
    isFire = False

    def __init__(self):
        self.sensorData = 0

    def getDataFromSensor(self):
        return self.sensorData

    def simulate_toggleFire(self):
        if not(self.isFire):
            self.sensorData = 50
            self.isFire = True
        else :
            self.sensorData = 0
            self.isFire = 0
