from threading import Thread
from CheckForFire import *
import publishSubscribe

class FireNotify(Thread):
    isThereFire = False
    roomNumber = 0
    fireChecker:CheckForFire
    publisherInstance:publishSubscribe.Publisher

    def __init__(self):
        self.publisherInstance = publishSubscribe.Publisher(5556)
        self.fireChecker = CheckForFire()
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            if self.fireChecker.detectFire():
                self.publisherInstance.publish(("[SmokeSensor] "+str(self.roomNumber)).encode())

    def simulate_toggleFire(self):
        self.fireChecker.simulate_toggleFire()

    def setRoomNumber(self, newNumber):
        self.roomNumber = newNumber
