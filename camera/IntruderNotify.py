from threading import Thread
from CheckForIntruder import *
import publishSubscribe

class IntruderNotify(Thread):
    intruderChecker:CheckForIntruder
    publisherInstance:publishSubscribe.Publisher

    def __init__(self):
        self.publisherInstance = publishSubscribe.Publisher(5556)
        self.intruderChecker = CheckForIntruder()
        Thread.__init__(self)
        self.start()

    def run(self):
        self.notifyIntruder()

    def notifyIntruder(self):
        while True:
            if self.intruderChecker.detectIntruder():
                print("INTRUSO")
                self.publisherInstance.publish(b"[Camera] INTRUSO DETECTADO")

    def simulate_toggleIntruder(self):
        self.intruderChecker.simulate_toggleIntruder()
