from threading import Thread
from CheckForBadWeather import *
import publishSubscribe

class BadWeatherNotify(Thread):
    isThereBadWeather = False
    badWeatherChecker:CheckForBadWeather
    publisherInstance:publishSubscribe.Publisher

    def __init__(self):
        self.publisherInstance = publishSubscribe.Publisher(5556)
        self.badWeatherChecker = CheckForBadWeather()
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            if self.badWeatherChecker.detectBadWeather():
                self.publisherInstance.publish(b"[RainSensor] MAU TEMPO DETECTADO")

    def simulate_toggleBadWeather(self):
        self.badWeatherChecker.simulate_toggleBadWeather()
