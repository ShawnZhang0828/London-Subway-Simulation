import sys

class AdjList():
    '''
        Adjlist class converts all connections to an adjacency list and 
        performs operations to obtain informations about the list
    '''
    
    def __init__(self, connection_list):
        '''
            Initialize a class instance
        '''
        self.setAdjList(connection_list)


    def setAdjList(self, connection_list):
        '''
            Convert all connections to an adjacency list
        '''
        self.adj_list = {}
        for connection in connection_list:
            if connection.s1 in self.adj_list:
                if connection.s2 in self.adj_list[connection.s1]:
                    self.adj_list[connection.s1][connection.s2].append((connection.line, connection.time))
                else:
                    self.adj_list[connection.s1][connection.s2] = [(connection.line, connection.time)]
            else:
                self.adj_list[connection.s1] = {}
                self.adj_list[connection.s1][connection.s2] = [(connection.line, connection.time)]
                
            # make the adjacency list symmetric (representing an undirected graph)
            if connection.s2 in self.adj_list:
                if connection.s1 in self.adj_list[connection.s2]:
                    self.adj_list[connection.s2][connection.s1].append((connection.line, connection.time))
                else:
                    self.adj_list[connection.s2][connection.s1] = [(connection.line, connection.time)]
            else:
                self.adj_list[connection.s2] = {}
                self.adj_list[connection.s2][connection.s1] = [(connection.line, connection.time)]
                
                
    def getOutEdges(self, station):
        '''
            Obtain all lines come out of station
            Sample output: [(station1, line2, 3), (station2, line4, 1), (station5, line1, 2)]
        '''
        out_edges = []
        for key, value in self.adj_list[station].items():
            for line, _ in value:
                # out_edges.append((key, line_info[0], line_info[1]))
                out_edges.append((key, line))
        return out_edges
        

    def getTime(self, station1, station2, line):
        '''
            Get the time that is needed to travel from station1 to station2 via a certain line
        '''
        try:
            for l in self.adj_list[station1][station2]:
                if l[0] == line:
                    return l[1]
            # return infinite if a line can't be found
            return sys.maxsize
        except:
            return sys.maxsize


    def getTimeWithoutLine(self, station1, station2):
        '''
            Get the time that is needed to travel from station1 to station2 without given the line
        '''
        try:
            return self.adj_list[station1][station2][0][1]
        except:
            raise KeyError
