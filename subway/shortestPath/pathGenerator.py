from subway.structures.itinerary import Itinerary

class PathGenerator():

    def __init__(self):
        self.allPath = []

    def dfs(self, edgeTo, current, start, visited, edges, connections):
        visited.append(current)

        for station in edgeTo[current]:
            if station[0] not in visited:
                current_edge = next((connection for connection in connections 
                                    if ((connection.s1 == station[0] and connection.s2 == current) or 
                                    (connection.s2 == station[0] and connection.s1 == current)) and 
                                        connection.line.id == station[1].id), None)
                if station[0].id == start.id:
                    self.allPath.append([current_edge] + edges)

                self.dfs(edgeTo, station[0], start, visited, [current_edge] + edges, connections)
            
        visited.remove(current)
        try:
            edges.pop(0)
        except:
            print('Last element has been popped.')


    def generatePath(self, edgeTo, start, end, connections):
        self.dfs(edgeTo, end, start, [], [], connections)

        itineraries = []
        for path in self.allPath:
            itineraries.append(Itinerary(start, end, path))

        return itineraries

    @staticmethod
    def printAllPath(all_path):
        for path in all_path:
            path.printItinerary()