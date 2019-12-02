from threading import Thread
from RetrieveCameraData import *
import publishSubscribe
from PIL import Image, ImageFile
import io
import pickle

class CameraFeedPublisher():
    cameraData:RetrieveCameraData
    publisherInstance:publishSubscribe.Publisher
    shouldPublishFrame = False

    def __init__(self, cameraData):
        self.publisherInstance = publishSubscribe.Publisher(5556)
        self.cameraData = cameraData
        Thread.__init__(self)

    def publishFrame(self):
        currentFrame = self.cameraData.getCameraFrame()

        currentFrameString = pickle.dumps(currentFrame)

        message = {
            'width': str(currentFrame.width),
            'height': str(currentFrame.height),
            'data': currentFrameString
        }

        messageString = pickle.dumps(message)

        self.publisherInstance.publish((b"[CameraFeed] "+messageString))



class CameraFeedSubscriber(publishSubscribe.Subscriber):
    cameraData:RetrieveCameraData
    feedPublisher:CameraFeedPublisher

    def __init__(self, cameraData):
        self.intruderChecker = cameraData
        self.feedPublisher = CameraFeedPublisher(cameraData)
        self.socketInit(["[CameraFeed]"], 5558)
        
    def messageReceived(self, message):
        self.feedPublisher.publishFrame()




class CameraFeed(Thread):

    def getCurrentFrame(self):
        return self.cameraData.getCameraFrame()

    feedSubscriber:CameraFeedSubscriber

    def run(self):
        while True:
            self.feedSubscriber.waitForMessage()

    def __init__(self, cameraData):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        self.cameraData = cameraData
        self.feedSubscriber = CameraFeedSubscriber(cameraData)
        Thread.__init__(self)
        self.start()
