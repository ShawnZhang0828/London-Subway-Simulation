from math import sqrt
import random
import string
from subway.structures.station import Station
from subway.structures.line import Line
from subway.structures.connection import Connection

class RandomGenerator():
    '''
        RandomGenerator class randomly generated a weighted undirected graph to simulate a subway system
    '''

    def __init__(self, station_num, line_num, line_density=0.1):
        '''
            Initialize a class instance
            line_density: probability of generating a path between two stations in a subway system
        '''
        self.s_num = station_num
        self.l_num = line_num
        self.l_density = line_density
        self.genStation()
        self.genLine()
        self.genConnection()


    def genStation(self):
        '''
            Generate a list of stations with id range from 0 to self.s_num and random names
        '''
        stations = []
        length = 1/self.s_num
        for i in range(self.s_num):
            stations.append(Station(i, 50+random.random(), -0.5+length+random.random(), 
                            RandomGenerator.genStr(), None, None, None, None))
            length += length
        self.s_list = stations

    
    def genLine(self):
        '''
            Generate a list of lines with id range from 0 to self.l_num and random names
        '''
        lines = []
        for i in range(self.l_num):
            lines.append(Line(i, RandomGenerator.genStr(), None, None))
        self.l_list = lines


    def genConnection(self):
        '''
            Randomly generate connections between stations use random lines, weights, and times
        '''
        connections = []
        for s1 in self.s_list:
            for s2 in self.s_list:
                if s1 != s2:
                    density_fac = sqrt(self.s_num / abs(s1.id - s2.id))
                    if random.random() < self.l_density * sqrt(density_fac):
                        line = random.choice(self.l_list)
                        connections.append(Connection(s1, s2, line, random.randint(1,4)))
                        # make it possible for multiple path between two stations
                        while random.random() < 0.2:
                            new_line = random.choice([l for l in self.l_list if l != line])
                            connections.append(Connection(s1, s2, new_line, random.randint(1,4)))
        self.c_list = connections


    @staticmethod
    def genStr():
        '''
            Generate a random string of length 5 to 12
        '''
        letters = string.ascii_letters
        length = random.randint(5,12)
        return ''.join(random.choice(letters) for _ in range(length))