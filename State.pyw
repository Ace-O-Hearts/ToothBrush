class brush():
    def __init__(self, user_name = ""):
        self.user_name = user_name
    
    def LED(self, led = ""):
        self.LED = led

class state():
    def __init__(self, state_name = ""):
        self.state_name = state_name
        
    def oscillation(self, rate, duty):
        self.frequency = rate
        self.cycle = duty

# frequency of the oscillation and duty cycle
# frequency between 1 and 1 kHz
# duty cycle between 0 and 1023 (512 is 50%)
    # May need to be changed if the frequency can be found for each setting

class Tooth(state):
    state_name = "Tooth"
    frequency = 100
    duty = 255
    
class Feather(state):
    state_name = "Feather"
    frequency = 100
    duty = 200
    
class Shine(state):
    state_name = "Shine"
    frequency = 100
    duty = 300
    
class Wave(state):
    state_name = "Wave"
    frequency = 200
    duty = 200

class User(state):
    state_name = "User Defined"
    frequency = 100
    duty = 100

class On(state):
    state_name = "On"
    frequency = 0
    duty = 0
