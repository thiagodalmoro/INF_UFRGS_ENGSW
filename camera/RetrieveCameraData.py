from PIL import Image

class RetrieveCameraData:
    noIntruderPath = "cameraFrameNoIntruder.jpg"
    intruderPath = "cameraFrameIntruder.jpg"
    isIntruder = False

    def __init__(self):
        self.currentFrame = Image.open(self.noIntruderPath)

    def getCameraFrame(self):
        if self.isIntruder:
            return Image.open(self.intruderPath)
        else:
            return Image.open(self.noIntruderPath)

    def simulate_toggleIntruder(self):
        if not(self.isIntruder):
            self.isIntruder = True
        else :
            self.isIntruder = False
