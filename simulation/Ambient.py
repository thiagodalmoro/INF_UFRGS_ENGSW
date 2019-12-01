from publishSubscribe import Publisher


class Ambient:

    publisherInstance = Publisher(5556)

    def __init__(self):
        pass

    def changeRoomState(self, state_type, data):
        message = "sensor_data_change %s:%d" % (state_type, data)
        self.publisherInstance.publish(bytes(message.encode()))

