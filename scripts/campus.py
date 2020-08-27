import numpy as np
from building import building

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self, numBuildings):
        self.buildings = { }
        self.makeBuildings(numBuildings)

    # instantiate buildings
    def makeBuildings(self, numBuildings):
        for i in range(numBuildings):
            self.buildings[i] = building(i, 4)

if __name__ == '__main__':
    c = campus(2)

    for building in c.buildings:
        for room in building:
            print(room)
