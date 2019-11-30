import sensorTemperatura


class Simulation:

    def __init__(self):
        self.initialize_sensors()

    def initialize_sensors(self):
        __sensor = sensorTemperatura.FireNotify(1)

