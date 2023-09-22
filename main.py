import time
time.sleep(0.1) # Wait for USB to become ready

from RoomController import *

print("Hello, Pi Pico!")

myroom = RoomController()

myroom.run()



