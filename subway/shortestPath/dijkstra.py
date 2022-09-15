import sys
import heapq
from subway.shortestPath.PrioritizedItem import PrioritizedItem
from subway.structures.itinerary import Itinerary


def dijkstra_algo(connection_list, stations, start_s):
    '''
        Implementation of the Dijkstra algorithm
    '''
    edgeTo = {}
    distTo = {}
    pq = []

    # initialize distances from the starting station
    for station in stations:
        distTo[station] = sys.maxsize
    distTo[start_s] = 0

    heapq.heappush(pq, PrioritizedItem(distTo[start_s], start_s))

    while pq:
        station = heapq.heappop(pq)
        # relax every edges(lines) adjacent to the current station
        try:
            out_edges = connection_list.getOutEdges(station.item)
        except Exception as e:
            print(f"A error has been detected!!! Error message: {e}")
            out_edges = []
        finally:
            for oe in out_edges:
                neighbor = oe[0]
                tentative_dist = distTo[station.item] + connection_list.getTime(station.item, neighbor, oe[1])
                # if current distance is less than previous distance, update the distTo[neighbour] value
                if distTo[neighbor] > tentative_dist:
                    distTo[neighbor] = tentative_dist
                    edgeTo[neighbor] = (station.item, oe[1])
                    if neighbor in [item.item for item in pq]:
                        heapq.heapreplace(pq, PrioritizedItem(distTo[neighbor], neighbor))  
                    else:
                        heapq.heappush(pq, PrioritizedItem(distTo[neighbor], neighbor))
    
    return edgeTo, distTo


def generatePath(edgeTo, start, end, connections):
    '''
        return the shortest path between start station and end station in order
    '''
    connection = []
    current = end
    # reverse track the edgeTo dictionary to obtain the path
    while True:
        previous = edgeTo[current][0]
        # find the appropriate connection object using two stations and line
        current_connection = next((connection for connection in connections 
                                if (connection.s1 == previous and connection.s2 == current) or 
                                   (connection.s2 == previous and connection.s1 == current) and 
                                    connection.line.id == edgeTo[current][1].id), None)
        print(current_connection)
        connection = [current_connection] + connection
        if previous.id == start.id:
            break
        current = edgeTo[current][0]
    # convert the connections to a itinerary object
    itinerary = Itinerary(start, end, connection)
    return itinerary
    