from subway.shortestPath.prioritizedItem import PrioritizedItem
from subway.shortestPath.pathGenerator import PathGenerator
import heapq

class ShortestPathAlgo():
    '''
        Abstract class for path finding algorithms
    '''

    def __init__(self, adj_list, station_list, connection_list, start_s, end_s):
        '''
            Initialize a class instance
        '''
        self.adjList = adj_list
        self.s_list = station_list
        self.c_list = connection_list
        self.start = start_s
        self.end = end_s


    def findShortestPath():
        pass


    def runAlgorithm(self):
        '''
            Run Dijkstra or A* to find shortest paths
            Output: A list of possible paths
        '''
        path_gen = PathGenerator()
        edgeTo, _ = self.findShortestPath()
        paths = path_gen.generatePath(edgeTo, self.start, self.end, self.c_list)
        return paths


    @staticmethod
    def updatePQ(pq, station, new_priority):
        prioritizedItem = next((i for i in pq if i.item == station), None)
        pq.remove(prioritizedItem)
        heapq.heappush(pq, PrioritizedItem(new_priority, station))
        return pq




    