from CheckForIntruder import *
import publishSubscribe
from threading import Thread

class CameraConfigurationSubscriber(publishSubscribe.Subscriber):

    intruderChecker:CheckForIntruder

    def __init__(self, intruderChecker):
        self.intruderChecker = intruderChecker
        self.socketInit(["[CameraConfig]"], 5558)
        
    def messageReceived(self, message):
        msg = message.split()
        config = msg[1]
        if(config == b"ActivateAlertMode"):
            self.intruderChecker.setAlertMode(True)
        elif(config == b"DeactivateAlertMode"):
            self.intruderChecker.setAlertMode(False)

class CameraConfiguration(Thread):
    configSubscriber:CameraConfigurationSubscriber

    def run(self):
        while True:
            self.configSubscriber.waitForMessage()

    def __init__(self, intruderChecker):
         self.configSubscriber = CameraConfigurationSubscriber(intruderChecker)
         Thread.__init__(self)
         self.start()