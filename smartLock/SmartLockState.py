class SmartLockState:

    def __init__(self):
        self.__smartLockState = True  # Initializing smartLockState

    def setSmartLockState(self, newState):
        self.__smartLockState = newState

    def getSmartLockState(self):
        return self.__smartLockState
