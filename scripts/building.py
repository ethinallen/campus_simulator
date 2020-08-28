import numpy as np
import random as rd
from room import room
from corridor import corridor

'''
    - Building has a modifier associated with it
        - modifies the input data given a mod equation
        - yields net sum associated with the output of the building
'''


class building:

    # initialize the sensor based on type and set age to 0
    def __init__(self, building_id, sensors_scale_val):

        self.id_num         = building_id
        self.building_mod   = None
        self.rooms          = { }
        self.corridors      = { }
        self.previous_power_consumption = None

        self.num_rooms = rd.randint(1, 5)
        self.num_corrs = rd.randint(1,3)

        self.makeRooms(self.num_rooms)
        self.makeCorridors(self.num_corrs)


    def makeRooms(self, number_rooms):
        for i in range(number_rooms):
            self.rooms[i] = room(i)

    def makeCorridors(self, number_corridors):
        for i in range(number_corridors):
            self.corridors[i] = corridor(i)

    def generate_power_consumption(self, theTime):
        self.previous_power_consumption = theTime * 13.4

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
