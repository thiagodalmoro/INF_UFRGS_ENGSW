from publishSubscribe import Publisher


class Ambient:

    __publisher_instance = Publisher(5556)

    def __init__(self):
        pass

    def change_room_state(self, state_type, data):
        message = "sensor_data_change %s:%d" % (state_type, data)
        self.__publisher_instance.publish(bytes(message.encode()))

