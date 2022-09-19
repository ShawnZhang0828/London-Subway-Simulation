import sys
import math
import heapq
from subway.shortestPath.shortestPathAlgo import ShortestPathAlgo
from subway.shortestPath.prioritizedItem import PrioritizedItem


class Astar(ShortestPathAlgo):

    @staticmethod
    def __h(current, end):
        '''
            heuristic function return the distance from current station to the destination
        '''
        # print(math.sqrt(math.pow(current.lat - end.lat, 2) + math.pow(current.lon - end.lon, 2)))
        return math.sqrt(math.pow(current.lat - end.lat, 2) + math.pow(current.lon - end.lon, 2)) * 50


    def findShortestPath(self):
        '''
            Implementation of the A* algorithm with the help of the heuristic function defined above
        '''
        edgeTo = {}
        distTo = {}
        totalCost = {}

        pq = []

        expanding_count = 0

        # initialize distance and total cost from starting station
        for station in self.s_list:
            distTo[station] = sys.maxsize
            totalCost[station] = sys.maxsize
            edgeTo[station] = []
        distTo[self.start] = 0
        totalCost[self.start] = 0

        heapq.heappush(pq, PrioritizedItem(totalCost[self.start], self.start))

        while pq:
            # expanding_count += 1
            station = heapq.heappop(pq)

            if station.item.id == self.end.id:
                # path = generatePath(edgeTo, start_s, end_s, connections)
                return edgeTo

            # relax all edges connected to the current station
            out_edges = self.c_list.getOutEdges(station.item)

            for oe in out_edges:
                neighbor = oe[0]
                tentative_dist = distTo[station.item] + self.c_list.getTime(station.item, neighbor, oe[1])
                # if the new distance to neighbor is shorter than the distance stored before, 
                # update distTo, edgeTo, totalCost, and the priority queue
                if distTo[neighbor] > tentative_dist:
                    distTo[neighbor] = tentative_dist
                    totalCost[neighbor] = tentative_dist + Astar.__h(neighbor, self.end)
                    # avoid duplicated items in edgeTo
                    if (station.item, oe[1]) not in edgeTo[neighbor]:
                        edgeTo[neighbor].append((station.item, oe[1]))
                    if neighbor in [item.item for item in pq]:
                        heapq.heapreplace(pq, PrioritizedItem(totalCost[neighbor], neighbor))
                    else:
                        heapq.heappush(pq, PrioritizedItem(totalCost[neighbor], neighbor))

        string = "I love coding"
        print(string)
        # print("edgeTo: ", edgeTo)
        # print("expanding_cunt: ", expanding_count)
        return edgeTo#, expanding_count
