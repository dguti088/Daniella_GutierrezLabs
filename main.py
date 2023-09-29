import time
time.sleep(0.1) # Wait for USB to become ready

from MemoryGameController import *
from Player import *

print("Hello, Pi Pico!")

memoryGame= MemoryGameController()

memoryGame.run()


