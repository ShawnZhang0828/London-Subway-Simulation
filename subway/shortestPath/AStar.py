import sys
import math
import heapq
from subway.shortestPath.PrioritizedItem import PrioritizedItem
from subway.shortestPath.dijkstra import generatePath


def h(current, end):
    '''
        heuristic function return the distance from current station to the destination
    '''
    return math.sqrt(math.pow(current.lat - end.lat, 2) + math.pow(current.lon - end.lon, 2))


def astar(connection_list, stations, start_s, end_s, connections):
    '''
        Implementation of the A* algorithm with the help of the heuristic function defined above
    '''
    edgeTo = {}
    distTo = {}
    totalCost = {}
    
    pq = []

    # initialize distance and total cost from starting station
    for station in stations:
        distTo[station] = sys.maxsize
        totalCost[station] = sys.maxsize
    distTo[start_s] = 0
    totalCost[start_s] = 0

    heapq.heappush(pq, PrioritizedItem(totalCost[start_s], start_s))

    while pq:
        station = heapq.heappop(pq)
        if station.item.id == end_s.id:
            path = generatePath(edgeTo, start_s, end_s, connections)
            return path
        # relax all edges connected to the current station
        try:
            out_edges = connection_list.getOutEdges(station.item)
        except Exception as e:
            print(f"A error has been detected!!! Error message: {e}")
            out_edges = []
        finally:
            for oe in out_edges:
                neighbor = oe[0]
                tentative_dist = distTo[station.item] + connection_list.getTime(station.item, neighbor, oe[1])
                # if the new distance to neighbor is shorter than the distance stored before, 
                # update distTo, edgeTo, totalCost, and the priority queue
                if distTo[neighbor] > tentative_dist:
                    distTo[neighbor] = tentative_dist
                    totalCost[neighbor] = tentative_dist + h(neighbor, end_s)
                    edgeTo[neighbor] = (station.item, oe[1])
                    if neighbor in [item.item for item in pq]:
                        heapq.heapreplace(pq, PrioritizedItem(totalCost[neighbor], neighbor))  
                    else:
                        heapq.heappush(pq, PrioritizedItem(totalCost[neighbor], neighbor))
        
    return -1

