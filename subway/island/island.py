import sys
from subway.shortestPath.aStar import Astar
from subway.shortestPath.pathGenerator import PathGenerator


class Island:
    '''

    '''

    def __init__(self, stations, connections, adjList):
        '''
            Initialize a class instance
        '''
        self.s_list = stations
        self.c_list = connections
        self.adjList = adjList

        self.zone_graph = {}
        self.island_graph = {}      # {zone: [[s1, s2], [s3]], zone: [[s4, s5, s6], [s7, s8], [s9]]}

        for s in self.s_list:
            if s.zone % 1 == 0:
                self.__initZoneGraph(int(s.zone), s)
            else:
                self.__initZoneGraph(int(s.zone+0.5), s)
                self.__initZoneGraph(int(s.zone-0.5), s)


    def __initZoneGraph(self, zone_num, station):
        '''
            Categorize a station into its correct zone_num list
        '''
        if zone_num in self.zone_graph:
            self.zone_graph[zone_num].append(station)
        else:
            self.zone_graph[zone_num] = [station]
            self.island_graph[zone_num] = []

    
    def findIslandinZone(self):
        '''
            Run DFS in each zone to identify islands
        '''
        for zone, stations in self.zone_graph.items():
            visited = []
            for station in stations:
                island = []
                if station not in visited:
                    island, visited = self.DFS(island, station, visited, zone)
                    self.island_graph[zone].append(island)


    def DFS(self, temp, current, visited, zone):
        '''
            DFS algorithm to search for islands
        '''
        visited.append(current)
        temp.append(current)

        for oe in self.adjList.getOutEdges(current):
            if oe[0] in self.zone_graph[zone]:
                if oe[0] not in visited:
                    temp, visited = self.DFS(temp, oe[0], visited, zone)
        
        return temp, visited


    def printIsland(self):
        '''
            Print out all islands in a graph
        '''
        for zone, islands in self.island_graph.items():
            print(f'\nIn zone{zone}, the islands are the following: ')
            for island in islands:
                print('------')
                for station in island:
                    print(station.id)


    def __findAllIsland(self, s):
        if s.zone % 1 == 0:
            for island in self.island_graph[s.zone]:
                if s in island:
                    return [island]
        else:
            zone = s.zone + 0.5
            for island in self.island_graph[zone]:
                if s in island:
                    island_list = [island]
            zone = s.zone - 0.5
            for island in self.island_graph[zone]:
                if s in island:
                    island_list.append(island)
            return island_list


    def findIslandConnection(self, *args):
        shortest_dist = sys.maxsize
        if len(args) == 2:
            for station1 in args[0]:
                for station2 in args[1]:
                    path_gen = PathGenerator()
                    astar_algo = Astar(self.adjList, self.s_list, station1, station2)
                    edgeTo, _ = astar_algo.findShortestPath()
                    paths = path_gen.generatePath(edgeTo, station1, station2, self.c_list)
                    if paths[0].travel_time < shortest_dist:
                        shortest_connection = paths[0]
            shortest_connection.printItinerary()
        else:
            for station1 in args[0]:
                for station2 in args[1]:
                    path_gen = PathGenerator()

                    astar_algo = Astar(self.adjList, self.s_list, station1, station2)
                    edgeTo, _ = astar_algo.findShortestPath()
                    paths = path_gen.generatePath(edgeTo, station1, station2, self.c_list)
                    if paths[0].travel_time < shortest_dist:
                        shortest_connection = paths[0]
            shortest_connection.printItinerary()
            for station1 in args[2]:
                for station2 in args[3]:
                    astar_algo = Astar(self.adjList, self.s_list, station1, station2)
                    edgeTo, _ = astar_algo.findShortestPath()
                    paths = path_gen.generatePath(edgeTo, station1, station2, self.c_list)
                    if paths[0].travel_time < shortest_dist:
                        shortest_connection = paths[0]
            shortest_connection.printItinerary()

    
    def findIslandInZone(self, s1, s2):
        '''
            pass
        '''
        # return if s1 and s2 do not belong to the same zone
        if s1.zone != s2.zone and abs(s1.zone - s2.zone) > 1:
            print(f'Station{s1.id} and Station{s2.id} are not in the same zone. Please try other stations.')
            return -1
        if s1.zone % 1 == 0 and s2.zone % 1 == 0 and abs(s1.zone - s2.zone) >= 1:
            print(f'Station{s1.id} and Station{s2.id} are not in the same zone. Please try other stations.')
            return -1

        if s1.zone % 1 == 0 and s2.zone % 1 != 0:
            island1 = self.__findAllIsland(s1)[0]
            island2 = self.__findAllIsland(s2)[1] if s2.zone - 0.5 == s1.zone else self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                return -1
            self.findIslandConnection(island1, island2)
        elif s1.zone % 1 != 0 and s2.zone % 1 == 0:
            island1 = self.__findAllIsland(s1)[1] if s1.zone - 0.5 == s2.zone else self.__findAllIsland(s1)[0]
            island2 = self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                return -1
            self.findIslandConnection(island1, island2)
        elif s1.zone % 1 == 0 and s2.zone % 1 == 0:
            island1 = self.__findAllIsland(s1)[0]; island2 = self.__findAllIsland(s2)[0]
            if s1 in island2 or s2 in island1:
                print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                return -1
            self.findIslandConnection(island1, island2)
        else:
            if s1.zone == s2.zone:
                island1 = self.__findAllIsland(s1)[0]
                island2 = self.__findAllIsland(s2)[0]
                island3 = self.__findAllIsland(s1)[1]
                island4 = self.__findAllIsland(s2)[1]
                if s1 in island2 or s2 in island1:
                    print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                    self.findIslandConnection(island3, island4)
                elif s1 in island4 or s2 in island3:
                    print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                    self.findIslandConnection(island1, island2)
                self.findIslandConnection(island1, island2, island3, island4)
            else:
                if s1.zone - 1 == s2.zone:
                    island1 = self.__findAllIsland(s1)[1]; island2 = self.__findAllIsland(s2)[0]
                    if s1 in island2 or s2 in island1:
                        print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                        return -1
                else:
                    island1 = self.__findAllIsland(s1)[0]; island2 = self.__findAllIsland(s2)[1]
                    if s1 in island2 or s2 in island1:
                        print(f'Station{s1.id} and Station{s2.id} are in the same island.')
                        return -1
                self.findIslandConnection(island1, island2)
            
