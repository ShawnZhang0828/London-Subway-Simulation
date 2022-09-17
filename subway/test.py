# from tools.plotter import plot

def main():
    from subway.utils.dataLoader import DataLoader

    data_loader = DataLoader('_dataset/london.stations - Test.csv', '_dataset/london.lines - Test.csv', '_dataset/london.connections - Test.csv')

    # stations = loadStation('_dataset/london.stations.csv')
    # lines = loadLine('_dataset/london.lines.csv')
    # connections = loadConnections('_dataset/london.connections.csv', stations, lines)

    stations = data_loader.loadStation()
    lines = data_loader.loadLine()
    connections = data_loader.loadConnections(stations, lines)

    from subway.shortestPath.adjList import AdjList
    from subway.shortestPath.dijkstra import Dijkstra
    from subway.shortestPath.aStar import Astar
    from subway.shortestPath.pathGenerator import PathGenerator

    adjList = AdjList(connections)
    start = stations[3]
    end = stations[7]
    dijkstra_algo = Dijkstra(adjList, stations, start, end)
    astar_algo = Astar(adjList, stations, start, end)
    path_gen = PathGenerator()
    edgeTo = dijkstra_algo.findShortestPath()
    # edgeTo = astar_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections)
    print()
    for path in paths:
        path.printItinerary()

        
    # path = astar(adjList, stations, start, end, connections)
    # print()
    # path.printItinerary()


if __name__ == "__main__":
    main()