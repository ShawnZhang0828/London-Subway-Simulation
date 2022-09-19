import pyperf
import random
import math

def dijkstra(stations, connections, start, end):
    from subway.shortestPath.adjList import AdjList
    from subway.shortestPath.dijkstra import Dijkstra
    from subway.shortestPath.pathGenerator import PathGenerator

    adjList = AdjList(connections)

    dijkstra_algo = Dijkstra(adjList, stations, start, end)
    path_gen = PathGenerator()
    edgeTo = dijkstra_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections)
    return paths


def aStar(stations, connections, start, end):
    from subway.shortestPath.adjList import AdjList
    from subway.shortestPath.aStar import Astar
    from subway.shortestPath.pathGenerator import PathGenerator

    adjList = AdjList(connections)

    astar_algo = Astar(adjList, stations, start, end)
    path_gen = PathGenerator()
    edgeTo = astar_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections)
    return paths


def findDistance(start, end):
    return math.sqrt(math.pow(start.lat - end.lat, 2) + math.pow(start.lon - end.lon, 2))

def main():
    # from subway.utils.randomGen import RandomGenerator

    # random_gen = RandomGenerator(100, 10, 0.10)
    # stations = random_gen.s_list
    # connections = random_gen.c_list
    # start_id = random.choice([i for i in range(0, 100)])
    # end_id = random.choice([i for i in range(0, 100) if i != start_id])
    # start = stations[start_id]
    # end = stations[end_id]
    
    from subway.utils.dataLoader import DataLoader

    data_loader = DataLoader('_dataset/london.stations.csv', '_dataset/london.lines.csv', '_dataset/london.connections.csv')

    stations = data_loader.loadStation()
    lines = data_loader.loadLine()
    connections = data_loader.loadConnections(stations, lines)

    start_id = random.choice([i for i in range(0, 290)])
    end_id = random.choice([i for i in range(0, 290) if i != start_id])
    start = stations[start_id]
    end = stations[end_id]

    print(findDistance(start, end))

    runner = pyperf.Runner()
    runner.bench_func("dijkstra", dijkstra, stations, connections, start, end)
    runner.bench_func("aStar", aStar, stations, connections, start, end)


if __name__ == "__main__":
    main()
    