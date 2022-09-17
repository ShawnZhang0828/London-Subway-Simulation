import sys
import heapq
from subway.shortestPath.shortestPathAlgo import ShortestPathAlgo
from subway.shortestPath.prioritizedItem import PrioritizedItem


class Dijkstra(ShortestPathAlgo):

    def findShortestPath(self):
        '''
            Implementation of the Dijkstra algorithm
        '''
        edgeTo = {}
        distTo = {}

        pq = []

        # initialize distances from the starting station
        for station in self.s_list:
            distTo[station] = sys.maxsize
            edgeTo[station] = []
        distTo[self.start] = 0

        heapq.heappush(pq, PrioritizedItem(distTo[self.start], self.start))

        while pq:
            station = heapq.heappop(pq)
            # relax every edges(lines) adjacent to the current station
            try:
                out_edges = self.c_list.getOutEdges(station.item)
            except Exception as e:
                print(f"A error has been detected!!! Error message: {e}")
                out_edges = []
            finally:
                for oe in out_edges:
                    neighbor = oe[0]
                    tentative_dist = distTo[station.item] + self.c_list.getTime(station.item, neighbor, oe[1])
                    # if current distance is less than previous distance, update the distTo[neighbour] value
                    if distTo[neighbor] > tentative_dist:
                        distTo[neighbor] = tentative_dist
                        # avoid duplicated items in edgeTo
                        if (station.item, oe[1]) not in edgeTo[neighbor]:
                            edgeTo[neighbor].append((station.item, oe[1]))
                        if neighbor in [item.item for item in pq]:
                            heapq.heapreplace(pq, PrioritizedItem(distTo[neighbor], neighbor))
                        else:
                            heapq.heappush(pq, PrioritizedItem(distTo[neighbor], neighbor))
        return edgeTo
    