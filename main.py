import time
import machine
import utime 
from Lights import * 
from Buzzer import *
from Displays import * 
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

#created instance of myLED light 
myled= Light(25, "Internal LED")

#turn on LED 
myled.on()

#wait for a few seconds 
utime.sleep(5)

#Turn off the LED 
myled.off()

extled = DimLight(22, "Pink Led")
extled.on()
utime.sleep(1)
extled.setBrightness(100)
utime.sleep(1)
extled.off()
extled.upDown()

mybuzzer = PassiveBuzzer(16)
mybuzzer.beep()

mydisplay = LCDDisplay(sda =0, scl =1, i2cid =0)
mydisplay.showText('Python is fun!')