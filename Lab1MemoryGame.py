from Button import * 
from Buzzer import * 
from Displays import * 
from Lights import *
from random import randint


#wait for USB to be ready 
time.sleep(0.1) 

print ("Hello, Welcome to Dani's Memory Game! :)") 

#class will provide logic for game using imported hardware classes 

class MemoryGame 
  def __init__(self):  
    self._display = LCDDisplay(sda = 0, scl = 1, i2cd = 0 )
    self._buzzer = PassiveBuzzer (16) 
    # self._button = Button that coencides with LED light
    self._buttonreset = Button(17, "reset", buttonhandler = self) 
    self._start() #start of game 

#setting up LEDs 
        redLED = Pin(22, Pin.OUT) 
        greenLED = Pin(21, Pin.OUT) 
        blueLED = Pin( 26, Pin.OUT)

  def startGame(self)
    self._notes.clear()
    self.duration = 200
    self._addcolor():
    while (self.readcolors() is True): 
      self.addcolor()

#user makes error 
    self.loseGame()
    self.play_all_colors(200) 
    self.waitStart
      

  


