import numpy as np
from sensor import sensor

'''
    - at least 1 thermostat
    -

'''
class corridor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_room_type):
        self.corridor_mod = None
        self.sensors = { }

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
