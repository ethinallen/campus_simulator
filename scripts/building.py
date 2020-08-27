import numpy as np
import random as rd
from room import room

'''
    - Building has a modifier associated with it
        - modifies the input data given a mod equation
'''


class building:

    # initialize the sensor based on type and set age to 0
    def __init__(self, building_id, number_rooms,):
        self.id_num         = building_id
        self.building_mod   = None
        self.corridors      = { }
        self.rooms          = { }

    # instantiate all rooms
    def makeRooms(self):



if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
