import publishSubscribe
from threading import Thread
from tkinter import *

class AlertModeConfigPublisher(publishSubscribe.Publisher):
    
    publisherInstance:publishSubscribe.Publisher = ""

    def __init__(self):
        self.publisherInstance = publishSubscribe.Publisher(5557)

    def activateAlertMode(self):
        self.publisherInstance.publish(b"[CameraConfig] ActivateAlertMode")
        self.publisherInstance.publish(b"[MovementSensorConfig] ActivateAlertMode")

    def deactivateAlertMode(self):
        self.publisherInstance.publish(b"[CameraConfig] DeactivateAlertMode")
        self.publisherInstance.publish(b"[MovementSensorConfig] DeactivateAlertMode")
        

class AlertModeConfig(Frame):
    thisPublisher:AlertModeConfigPublisher = ""
    thisMaster = ""
    isAlertMode = False
    toggleAlert = ""

    def __init__(self, master=None):
        
        self.thisPublisher = AlertModeConfigPublisher()

        self.thisMaster = master

        self.widget = Frame(master)
        self.widget.pack()

        self.toggleAlert = Checkbutton(self.widget, text="Modo Alerta desativado")
        self.toggleAlert["command"] = self.toggleAlertMode
        self.toggleAlert.pack()

    def toggleAlertMode(self):
        if(self.isAlertMode):
            self.thisPublisher.deactivateAlertMode()
            self.toggleAlert["text"] = "Modo Alerta desativado"
            self.isAlertMode = False
        else:
            self.thisPublisher.activateAlertMode()
            self.toggleAlert["text"] = "Modo Alerta ativado"
            self.isAlertMode = True
