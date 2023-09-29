"""
A basic template file for using the Model class in PicoLibrary
This will allow you to implement simple Statemodels with some basic
event-based transitions.

Currently supports only 4 buttons (hardcoded to BTN1 through BTN4)
and a TIMEOUT event for internal tranisitions.

For processing your own events such as sensors, you can implement
those in your run method for transitions based on sensor events.
"""

# Import whatever Library classes you need - Model is obviously needed
import random
import time
from Model import *
from Button import *
from Lights import *  
from Buzzer import *
import utime

"""
This is the template Model Runner - you should rename this class to something
that is supported by your class diagram. This should associate with your other
classes, and any PicoLibrary classes. If you are using Buttons, you will implement
buttonPressed and buttonReleased.

To implement the model, you will need to implement 3 methods to support entry actions,
exit actions, and state actions.

This template currently implements a very simple state model that uses a button to
transition from state 0 to state 1 then a 5 second timer to go back to state 0.
"""
class Player: 
    def__init__(self): 
        self.input_sequence = []    
    def get_input(self): 
        #simulate player input 
        #input._value = input 
        self.input_sequence.append(input_value)           


class MemoryGameController:

    def __init__(self, player):
        
        # Instantiate whatever classes from your own model that you need to control
        # Handlers can now be set to None - we will add them to the model and it will
        # do the handling
        self._startButton = Button(10, "startButton", buttonhandler=None)
        self._resetButton = Button(11, "resetButton", buttonhandler=None)
        self._timer = SoftwareTimer(None)
        self._button1 = Button(0, 'gameButton1')
        self._button2 = Button (1, 'gameButton2')
        self._button3 = Button (2, 'gameButton3')
        self._button4 = Button (3, 'gameButton4')
        self._mybuzzer = PassiveBuzzer(15)
        self._display = LCDDisplay(sda=28, scl=27, i2cid=28)
        self.random 
        self._led = [machine.Pin(0, machine.Pin.OUT), 
            machine.Pin(1, machine.Pin.OUT),
            machine.Pin(2, machine.Pin.OUT),
            machine.Pin(3, machine.Pin.OUT)]

                # Define a list of LED colors or symbols
                colors = ["Red", "Green", "Blue", "Yellow"]
          def generate_random_sequence(length):
            return [random.choice(colors) for _ in range(length)]   
           levels = [
                [1, 2, 3],
                [4, 5, 6, 7],
                
            ]


        # Instantiate a Model. Needs to have the number of states, self as the handler
        # You can also say debug=True to see some of the transitions on the screen
        # Here is a sample for a model with 4 states
        self._model = Model(5, self, debug=True)
        
        # Up to 4 buttons and a timer can be added to the model for use in transitions
        # Buttons must be added in the sequence you want them used. The first button
        # added will respond to BTN1_PRESS and BTN1_RELEASE, for example
        self._model.addButton(self._startButton)
        self._model.addButton(self._resetButton)
        # add other buttons (up to 3 more) if needed
        
        # Add any timer you have.
        self._model.addTimer(self._timer)
        
        # Now add all the transitions that are supported by my Model
        # obvously you only have BTN1_PRESS through BTN4_PRESS
        # BTN1_RELEASE through BTN4_RELEASE
        # and TIMEOUT
        
        # some examples:
        self._model.addTransition(0, [BTN1_PRESS], 1)
        self._model.addTransition(1, [BTN2_PRESS],2)
        # etc.
    
    """
    Create a run() method - you can call it anything you want really, but
    this is what you will need to call from main.py or someplace to start
    the state model.
    """

    def run(self):
        # The run method should simply do any initializations (if needed)
        # and then call the model's run method.
        # You can send a delay as a parameter if you want something other
        # than the default 0.1s. e.g.,  self._model.run(0.25)
        self._model.run()

    """
    stateDo - the method that handles the do/actions for each state
    """
    def stateDo(self, state):
            
        # Now if you want to do different things for each state you can do it:
        if state == 1:
            # State 1 do/actions
            if self._self.input_sequence.append(input_value)
                self._model.gotoState(2)
        elif state == 2:
            # State1 do/actions
            # You can check your sensors here and perform transitions manually if needed
            # For example, if you want to go from state 1 to state 2 when the motion sensor
            # is tripped you can do something like this
            # if self.motionsensor.tripped():
            # 	gotoState(2)
            self._notifyplayer.display.showText()
            self._timer.check()
        elif state ==3: 
            self._incrementScore(int)    

    """
    stateEntered - is the handler for performing entry/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    """
    def stateEntered(self, state, event):
        # Again if statements to do whatever entry/actions you need
        if state == 0:
            # entry actions for state 0
            print('Hi! Welcome to Danis Game of Memory!')
        
        
        elif state == 1:
            # entry actions for state 1
            print('State 1 entered')
           def play_level(level):
                random.shuffle(level)
                print("Memorize the sequence:")
             print(level)
            for color in sequence:
            for led in led_pins:
            led.value(1)  # Turn on the LED
            utime.sleep_ms(500)  # Wait for 500 milliseconds
            led.value(0)  # Turn off the LED
            utime.sleep_ms(100)  # Wait for 100 milliseconds

        elif state == 2:
            print ('State 2 entered')
            self._checkInput()
        
        elif state == 3: 
            get_input()

        elif state == 4: 
            def _notifyplayer.Display.showText(
            print 'You Lose') 

        elif state == 5:    
            def _notifyplayer.Display.showText(
            print 'You Win!')

        
            
    """
    stateLeft - is the handler for performing exit/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    
    This is just like stateEntered, perform only exit/actions here
    """

    def stateLeft(self, state, event):
        if state == 0:
            # EXIT actions for state 1
            print('Lets Go Player 1!')
            self._startButton()

        elif state == 1:
            print ('State 1 exited')
            self._recieveInput()

        elif state ==2:    
            self.input_sequence.append(input_value)
                    
            for i, level in enumerate(levels):
                print(f"Level {i + 1}")
        
        # Play the current level
        success = play_level(level)
        
        if not success:
            print(f"You reached level {i + 1}. Try again.")
            break
        elif i == len(levels) - 1:
            print("Congratulations! You've won the game!")

    

# Test your model. Note that this only runs the template class above
# If you are using a separate main.py or other control script,
# you will run your model from there.
if __name__ == '__main__':
    MyControllerTemplate().run()