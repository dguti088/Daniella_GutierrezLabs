from Button import * 
from Buzzer import * 
from Displays import * 
from Lights import *

#wait for USB to be ready 
time.sleep(0.1) 

print ("Hello, Welcome to Dani's Memory Game! :)") 

#class will provide logic for game using imported classes 

class MemoryGame 
def __init__(self):  
  self._display = LCDDisplay(sda = 0, scl = 1, i2cd = 0 )
  self._buzzer = PassiveBuzzer (16) 
  self-_
  self._buttonreset = Button(17, "reset", buttonhandler = self) 
  self._start() #start of game 
  


