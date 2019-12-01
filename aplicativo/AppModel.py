class AppModel:

    def __init__(self):
        self.smartlock = []
        self.fingerprints = []

    def getSmartlockState(self, smartlockID):
        return self.smartlock[smartlockID]

    def setSmartlockState(self, smartlockID):
        if self.smartlock[smartlockID]:
            self.smartlock[smartlockID] = False
        else:
            self.smartlock[smartlockID] = True

    def setNewFingerprint(self, fingerprintData):
        self.fingerprints += fingerprintData

    def checkIfValidFingerprint(self, fingerprintData):
        if fingerprintData in self.fingerprints:
            return True
        else:
            return False
