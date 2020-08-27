import numpy as np
'''
    - at least 1 thermostat
    -

'''
class room:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_room_type):
        self.room_mod   = None
        self.sensors    = { }

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
