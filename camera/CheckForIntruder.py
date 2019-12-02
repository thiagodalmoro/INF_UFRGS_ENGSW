from RetrieveCameraData import *
from PIL import Image
from PIL import ImageChops

class CheckForIntruder:
    cameraData:RetrieveCameraData
    isAlertModeActive = False

    def __init__(self):
        self.cameraData = RetrieveCameraData()

    def detectIntruder(self):
        frame_no_intruder = Image.open("cameraFrameNoIntruder.jpg")
        current_frame = self.cameraData.getCameraFrame()

        diff = ImageChops.difference(frame_no_intruder, current_frame)

        if diff.getbbox() and self.isAlertModeActive:
            return True
        else:
            return False

    def setAlertMode(self, isActive):
        self.isAlertModeActive = isActive

    def simulate_toggleIntruder(self):
        self.cameraData.simulate_toggleIntruder()
