import random
import math
import time

def dijkstra(stations, connections, start, end):
    from subway.shortestPath.adjList import AdjList
    from subway.shortestPath.dijkstra import Dijkstra
    from subway.shortestPath.pathGenerator import PathGenerator

    adjList = AdjList(connections)

    dijkstra_algo = Dijkstra(adjList, stations, connections, start, end)
    path_gen = PathGenerator()
    edgeTo, expanding_count = dijkstra_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections)

    # print(f'Ratio used/explored for Dijkstra: {path_gen.countStations()/expanding_count}')

    return paths, path_gen.countStations()/expanding_count


def aStar(stations, connections, start, end):
    from subway.shortestPath.adjList import AdjList
    from subway.shortestPath.aStar import Astar
    from subway.shortestPath.pathGenerator import PathGenerator

    adjList = AdjList(connections)

    astar_algo = Astar(adjList, stations, connections, start, end)
    path_gen = PathGenerator()
    edgeTo, expanding_count = astar_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections)

    # print(f'Ratio used/explored for A*: {path_gen.countStations()/expanding_count}')

    return paths, path_gen.countStations()/expanding_count


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

    dijkstra_times = []
    astar_times = []
    dijkstra_ratios = []
    astar_ratios = []
    distances = []

    test_num = 200

    for i in range(test_num):
        start_id = random.choice([i for i in range(0, 290)])
        end_id = random.choice([i for i in range(0, 290) if i != start_id])
        start = stations[start_id]
        end = stations[end_id]

        distances.append(findDistance(start, end))

        for i in range(10):
            start_time = time.time()
            _, ratio = dijkstra(stations, connections, start, end)
            dijkstra_times.append(time.time() - start_time)
            dijkstra_ratios.append(ratio * 100)

        for i in range(10):
            start_time = time.time()
            _, ratio = aStar(stations, connections, start, end)
            astar_times.append(time.time() - start_time)
            astar_ratios.append(ratio * 100)


    print(f'Average time for Dijkstra: {sum(dijkstra_times) / len(dijkstra_times)}\nAverage time for A*: {sum(astar_times) / len(astar_times)}')
    print(f'Average usage ratio for Dijkstra: {sum(dijkstra_ratios) / len(dijkstra_ratios)}\nAverage usage ratio for A*: {sum(astar_ratios) / len(astar_ratios)}')

    dijkstra_time = [sum(dijkstra_times[10*i: 10*(i+1)]) / 10 for i in range(test_num)]
    astar_time = [sum(astar_times[10*i: 10*(i+1)]) / 10 for i in range(test_num)]
    dijkstra_ratio = [sum(dijkstra_ratios[10*i: 10*(i+1)]) / 10 for i in range(test_num)]
    astar_ratio = [sum(astar_ratios[10*i: 10*(i+1)]) / 10 for i in range(test_num)]

    all_info = [(distances[i], dijkstra_time[i], astar_time[i], dijkstra_ratio[i], astar_ratio[i]) for i in range(len(distances))]
    all_info.sort(key=lambda info : info[0])

    distances = [info[0] for info in all_info]
    dijkstra_time = [info[1] for info in all_info]
    astar_time = [info[2] for info in all_info]
    dijkstra_ratio = [info[3] for info in all_info]
    astar_ratio = [info[4] for info in all_info]

    import matplotlib.pyplot as plt

    plt.figure(0)
    plt.plot(distances, dijkstra_time, label="dijkstra")
    plt.plot(distances, astar_time, label="aStar")
    plt.legend()
    plt.title('Distance between Stations vs. Execution Time')
    plt.xlabel('Distances')
    plt.ylabel('Execution Time (ms)')

    plt.figure(1)
    plt.plot(distances, dijkstra_ratio, label="dijkstra")
    plt.plot(distances, astar_ratio, label="aStar")
    plt.legend()
    plt.title('Distance between Stations vs. Explored Stations Used Ratio (%)')
    plt.xlabel('Distances')
    plt.ylabel('Explored Stations Used Ratio (%)')

    plt.show()


if __name__ == "__main__":
    main()
    