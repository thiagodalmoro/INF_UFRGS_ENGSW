import time

from simulation.Ambient import Ambient

ambient = Ambient()

while True:
    ambient.changeRoomState("smoke", 50)
    time.sleep(1)
