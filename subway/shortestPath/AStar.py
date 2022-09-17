import sys
import math
import heapq
from subway.shortestPath.shortestPathAlgo import ShortestPathAlgo
from subway.shortestPath.prioritizedItem import PrioritizedItem



class Astar(ShortestPathAlgo):

    @staticmethod
    def h(current, end):
        '''
            heuristic function return the distance from current station to the destination
        '''
        return math.sqrt(math.pow(current.lat - end.lat, 2) + math.pow(current.lon - end.lon, 2))


    def findShortestPath(self):
        '''
            Implementation of the A* algorithm with the help of the heuristic function defined above
        '''
        edgeTo = {}
        distTo = {}
        totalCost = {}

        pq = []

        # initialize distance and total cost from starting station
        for station in self.s_list:
            distTo[station] = sys.maxsize
            totalCost[station] = sys.maxsize
            edgeTo[station] = []
        distTo[self.start] = 0
        totalCost[self.start] = 0

        heapq.heappush(pq, PrioritizedItem(totalCost[self.start], self.start))

        while pq:
            station = heapq.heappop(pq)

            # relax all edges connected to the current station
            try:
                out_edges = self.c_list.getOutEdges(station.item)
            except Exception as e:
                print(f"A error has been detected!!! Error message: {e}")
                out_edges = []
            finally:
                for oe in out_edges:
                    neighbor = oe[0]
                    tentative_dist = distTo[station.item] + self.c_list.getTime(station.item, neighbor, oe[1])
                    # if the new distance to neighbor is shorter than the distance stored before, 
                    # update distTo, edgeTo, totalCost, and the priority queue
                    if distTo[neighbor] > tentative_dist:
                        distTo[neighbor] = tentative_dist
                        totalCost[neighbor] = tentative_dist + Astar.h(neighbor, self.end_s)
                        # avoid duplicated items in edgeTo
                        if (station.item, oe[1]) not in edgeTo[neighbor]:
                            edgeTo[neighbor].append((station.item, oe[1]))
                        if neighbor in [item.item for item in pq]:
                            heapq.heapreplace(pq, PrioritizedItem(totalCost[neighbor], neighbor))
                        else:
                            heapq.heappush(pq, PrioritizedItem(totalCost[neighbor], neighbor))

        return edgeTo


