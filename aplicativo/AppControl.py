from aplicativo.AppModel import AppModel
from aplicativo.AppView import AppView


class AppControl:

    def __init__(self):
        self.__appModel = AppModel()
        self.__appView = AppView(self.__appModel)

    def processUIInputEvent(self):
        pass

    def fireNotificationHandler(self):
        pass

    def rainNotificationHandler(self):
        pass

    def intruderNotificationHandler(self):
        pass

    def toggleAlertMode(self):
        pass

    def setSmartLockState(self):
        pass

