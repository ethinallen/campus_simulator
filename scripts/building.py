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
    def __init__(self, building_id, number_rooms, sensors_scale_val):

        self.id_num         = building_id
        self.building_mod   = None
        self.rooms          = { }
        self.corridors      = { }
        self.previous_power_consumption = None

        self.makeRooms(rd.randint(5,10))
        self.makeCorridors(rd.randint(5,10))

    def makeRooms(self, number_rooms):
        for i in range(number_rooms):
            self.rooms[i] = room('thermostat')

    def makeCorridors(self, number_corridors):
        for i in range(number_corridors):
            self.corridors[i] = room('thermostat')

    def generate_power_consumption(self, time):
        self.previous_power_consumption = time * 13.4

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
