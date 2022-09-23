from subway.shortestPath.prioritizedItem import PrioritizedItem
import heapq

class ShortestPathAlgo():
    '''
        Abstract class for path finding algorithms
    '''

    def __init__(self, connection_list, station_list, start_s, end_s):
        '''
            Initialize a class instance
        '''
        self.c_list = connection_list
        self.s_list = station_list
        self.start = start_s
        self.end = end_s


    def findShortestPath():
        pass

    @staticmethod
    def updatePQ(pq, station, new_priority):
        prioritizedItem = next((i for i in pq if i.item == station), None)
        pq.remove(prioritizedItem)
        heapq.heappush(pq, PrioritizedItem(new_priority, station))
        return pq




    