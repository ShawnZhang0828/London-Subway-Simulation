class Itinerary():
    '''
        Itinerary class is used to represent the path from stating station to ending station,
        including all the connections between
    '''

    def __init__(self, s1, s2, connections):
        '''
            Initialize a class instance
        '''
        self.s1 = s1
        self.s2 = s2
        self.connections = connections
        self.setTravelT()
        self.setTransferT()

    def setTravelT(self):
        '''
            Calculate the travel time of the path
        '''
        self.travel_time = sum([c.time for c in self.connections])

    def setTransferT(self):
        '''
            Calculate the transfer time of the path
        '''
        self.transfer_time = 0
        for i, connection in enumerate(self.connections[:-1]):
            if connection.line != self.connections:
                self.transfer_time += 1

    def printItinerary(self):
        '''
            print the path
        '''
        current = self.s1
        print(current.id, f' - via line{self.connections[0].line.id} - ', end="")
        for i, connection in enumerate(self.connections):
            if connection.s1 == current:
                print(f'{connection.s2.id} - via line{self.connections[i+1].line.id} - ', end="") if i != len(self.connections) - 1 else print(f'{connection.s2.id}', end="")
                current = connection.s2
            else:
                print(f'{connection.s1.id} - via line{self.connections[i+1].line.id} - ', end="") if i != len(self.connections) - 1 else print(f'{connection.s1.id}', end="")
                current = connection.s1
        print(f'\nTransfer times: {self.transfer_time}  -  Travel time: {self.travel_time}\n')
