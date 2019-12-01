from simulation.FingerprintSensor import FingerprintSensor


class AppView:

    def __init__(self, appModel):
        self.__appModel = appModel
        self.__fingerprintSensor = FingerprintSensor()  # Only for simulation

    def __renderAppUI(self, isAlertOn):
        pass  # Draw UI on app, tkinter

    def __notifyAppInputEvent(self):
        pass  # Send info to AppControl

    def __readFingerprintData(self):
        pass  # Reads

    def __saveFingerprintData(self):
        pass

    def showAlertMessage(self):
        self.__renderAppUI(True)
