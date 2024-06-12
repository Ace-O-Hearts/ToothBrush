
"""
Tooth Brush Description:
- Has 4 states
    - Tooth
    - Feather
    - Shine
    - Wave
- when running, the LED ring turns red when enough pressure is applied to the brush head regardless of the state it is in
- LED indicator light for battery level at the bottom of the brush handle
    - has 3 segments
    - flashes when charging to indicate current charge level
- Bluetooth connectivity with a mobile application
    - App can be used to:
        - track brush movements
        - change LED color
        - adjust settings for some of the brush states
        
How are the brush oscillations of each setting determined?
    - Fixed frequency and increasing duty cycle?
"""

import math
import time
import wave
import machine
#from State import brush, state
import State

int power = 0;
int pressure = 0;
int Button = 0;

# Move to Bluetooth section later
usr_name = str(input('What is your name: '))
user_def = str(input('Color of your brush: '))
# Move to Bluetooth section later

# Use the the following block to enable/disable interrupts
'''
state = machine.disable_irq()
machine.enable_irq(state)
'''

# Brush setup
Brush = State.brush()
Brush.user_name(usr_name)

# Need to implement some kind of interrupt to change the LED to RED if the user is pressing on the brush head too hard and then revert when they're not
Brush.LED(user_def)

# Move states to state.pyw for compartmentalizing?
"""
Tooth = State.state()
Tooth.statename = "Tooth"

# Maybe predefine these for each state and then have this at the end for the user to define a state
'''
frequency = int(input("Speed: "))
while frequency < 1 or frequency > 1000:
    frequency = 100 # in terms of Hz
duty = int(input("How often: "))
while duty < 0 or duty > 1023:
    duty = 255 # scale is from 0 to 1023

frequency = 100 # in terms of Hz
duty = 255 # scale is from 0 to 1023
'''

Tooth.oscillation(100, 255)                      # frequency of the oscillation and duty cycle
                                                 # frequency between 1 and 1 kHz
                                                 # duty cycle between 0 and 1023 (512 is 50%)
                                                   # May need to be changed if the frequency can be found for each setting

Feather = State.state()
Feather.statename = "Feather"

# Maybe predefine these for each state and then have this at the end for the user to define a state
'''
frequency = int(input("Speed: "))
while frequency < 1 or frequency > 1000:
    frequency = int(input("Speed: "))
duty = int(input("How often: "))
while duty < 0 or duty > 1023:
    duty = int(input("How often: "))
'''

frequency = 100 # in terms of Hz
duty = 255 # scale is from 0 to 1023

Feather.oscillation(frequency, duty)                      # frequency of the oscillation and duty cycle
                                                          # frequency between 1 and 1 kHz
                                                          # duty cycle between 0 and 1023 (512 is 50%)
                                                            # May need to be changed if the frequency can be found for each setting

Shine = State.state()
Shine.statename = "Shine"

# Maybe predefine these for each state and then have this at the end for the user to define a state
'''
frequency = int(input("Speed: "))
while frequency < 1 or frequency > 1000:
    frequency = int(input("Speed: "))
duty = int(input("How often: "))
while duty < 0 or duty > 1023:
    duty = int(input("How often: "))
'''

frequency = 100 # in terms of Hz
duty = 255 # scale is from 0 to 1023

Shine.oscillation(frequency, duty)                      # frequency of the oscillation and duty cycle
                                                        # frequency between 1 and 1 kHz
                                                        # duty cycle between 0 and 1023 (512 is 50%)
                                                          # May need to be changed if the frequency can be found for each setting

Wave = State.state()
Wave.statename = "Wave"

# Maybe predefine these for each state and then have this at the end for the user to define a state
'''
frequency = int(input("Speed: "))
while frequency < 1 or frequency > 1000:
    frequency = int(input("Speed: "))
duty = int(input("How often: "))
while duty < 0 or duty > 1023:
    duty = int(input("How often: "))
'''

frequency = 100 # in terms of Hz
duty = 255 # scale is from 0 to 1023

Wave.oscillation(frequency, duty)                      # frequency of the oscillation and duty cycle
                                                       # frequency between 1 and 1 kHz
                                                       # duty cycle between 0 and 1023 (512 is 50%)
                                                         # May need to be changed if the frequency can be found for each setting
"""
class position_switch():
    def position(self, position):
        
        return getattr("case_" + str(position))

    def case_1(self):
        State.Tooth()
        
    def case_2(self):
        State.Feather()
        
    def case_3(self):
        State.Shine()
        
    def case_4(self):
        State.Wave()
        
    def case_5(self):
        State.user()
        
        # User defined, needs bluetooth to be updated from default values
    def case_default(self):
        State.On()
        

class update_pressure():
    def __init__(self):
        #return pressure = "p##"
        # Will return a value from a specific pin
        return

position = 0
 
# Approach incomplete and only usable on python 3.10 or newer
"""
while(power!=0){
    match position:
        case 1:
            State.Tooth()
        case 2:
            State.Feather()
        case 3:
            State.Shine()
        case 4:
            State.Wave()
        case default:
            State.On()
}
"""

while (power == 1):
    position_switch.position(position)
    if(Button == 1):
        pressed.button()
    
    
    # test statement
    print(f"state is {State.statename}, LED color is {Brush.LED}, Frequency and Duty cycle are {State.frequency} and {State.duty}")


# need to incorporate as an interrupt to indicate to user that they are applying too much pressure
class too_much_pressure():
    while (pressure >= 100):
        Brush.LED("RED")
        pressure = update_pressure()
        if (pressure < 100):
            Brush.LED = user_def
            break
        
class pressed():    # button was pressed increment position by 1
    def button(self):
        position += 1
        if (position > 5):
            position = 1
    

#There is bluetooth connectivity with a companion mobile app, but I don't have any understanding on how to program that