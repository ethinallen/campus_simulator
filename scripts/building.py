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
    def __init__(self, building_id, numRows, *attrs):

        self.rooms                      = { }
        self.corridors                  = { }

        if attrs:
            attrs=attrs[0]
            self.id = attrs['id']
            self.stdev = attrs['info']['stdev']
            self.adjustment = attrs['info']['adjustment']

            for roomID in attrs['info']['rooms']:
                room_attributes = {'id': roomID, 'info' : attrs['info']['rooms'][roomID]}
                self.rooms[roomID] = room(0, numRows, room_attributes)

            for corridorID in attrs['info']['corridors']:
                corridor_attributes = {'id': corridorID, 'info' : attrs['info']['corridors'][corridorID]}
                self.corridors[corridorID] = corridor(0, numRows, corridor_attributes)

        else:
            num_buildings = np.random.poisson(10, 1)[0]

            self.id                         = building_id
            self.building_mod               = None

            self.stdev = int(np.random.poisson(50, 1)[0])
            self.adjustment = int(np.random.normal(0, 100, 1)[0])
            self.entropy = np.random.normal(0, self.stdev, numRows)

            self.num_rooms = rd.randint(1, 10)
            self.num_corrs = rd.randint(1,15)

            self.makeRooms(numRows)


    def makeRooms(self, numRows):
        for i in range(self.num_rooms):
            self.rooms[i] = room(i, numRows)

        for i in range(self.num_corrs):
            self.corridors[i] = corridor(i, numRows)

    def generate_power_consumption(self, rowData, index):
        powerConsumption = rowData + self.adjustment + self.entropy[index]
        return powerConsumption

if __name__ == '__main__':
    s = sensor('thermostat')
