import pytest
from subway.structures.connection import Connection
from subway.structures.line import Line
from subway.structures.station import Station
from subway.utils.dataLoader import DataLoader
from subway.utils.metricsHandler import MetricsHandler

from subway.shortestPath.adjList import AdjList
from subway.shortestPath.dijkstra import Dijkstra
from subway.shortestPath.aStar import Astar
from subway.shortestPath.pathGenerator import PathGenerator


file_paths_1 = ['_dataset/london.stations.csv', '_dataset/london.lines.csv', '_dataset/london.connections.csv']
file_paths_2 = ['_dataset/london.stations - Test.csv', '_dataset/london.lines - Test.csv', '_dataset/london.connections - Test.csv']

data_loader_1 = DataLoader(file_paths_1[0], file_paths_1[1], file_paths_1[2])
data_loader_2 = DataLoader(file_paths_2[0], file_paths_2[1], file_paths_2[2])

stations_1 = data_loader_1.loadStation()
lines_1 = data_loader_1.loadLine()
connections_1 = data_loader_1.loadConnections(stations_1, lines_1)

stations_2 = data_loader_2.loadStation()
lines_2 = data_loader_2.loadLine()
connections_2 = data_loader_2.loadConnections(stations_2, lines_2)

def test_loadData_2():
    global stations_1, lines_1, connections_1
    
    data_loader = DataLoader(file_paths_2[0], file_paths_2[1], file_paths_2[2])

    stations = data_loader.loadStation()
    lines = data_loader.loadLine()
    connections = data_loader.loadConnections(stations, lines)
    assert [station.lat for station in stations] == [51.5028, 51.5143, 51.5154, 51.5107, 51.5407, 51.5322, 51.5653, 51.6164, 51.4905]
    assert [line.name for line in lines] == ["Bakerloo Line", "Circle Line", "Hammersmith & City Line", "Jubilee Line", "Victoria Line"]
    assert [connection.time for connection in connections] == [3, 2, 3, 1, 1, 3, 1, 3, 2, 4, 1, 2, 1, 4, 3, 2, 3, 6, 4, 3]


def test_metrics_2():
    metrics_handler = MetricsHandler(stations_2, lines_2, connections_2)

    num_nodes = metrics_handler.computeNodeNum()
    num_edges = metrics_handler.computeEdgeNum()
    avg_deg = round(metrics_handler.computeAvgDeg(), 2)
    assert num_nodes == 9
    assert num_edges == 20
    assert avg_deg == 4.44


def test_dijkstra_2():
    global connections_2, stations_2, lines_2
    adjList = AdjList(connections_2)
    start = stations_2[3]
    end = stations_2[7]

    dijkstra_algo = Dijkstra(adjList, stations_2, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = dijkstra_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections_2)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    assert stations_in_path == {4, 3, 1, 8}


def test_astar_2():
    global connections_2, stations_2, lines_2
    adjList = AdjList(connections_2)
    start = stations_2[3]
    end = stations_2[7]

    astar_algo = Astar(adjList, stations_2, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = astar_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections_2)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    assert stations_in_path == {4, 3, 9, 2, 8}


def test_dijkstra_1():
    global connections_1, stations_1, lines_1
    adjList = AdjList(connections_1)
    start = stations_1[171]
    end = stations_1[219]

    dijkstra_algo = Dijkstra(adjList, stations_1, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = dijkstra_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections_1)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    assert stations_in_path == {197, 151, 60, 126, 48, 250}


def test_astar_1():
    global connections_1, stations_1, lines_1
    adjList = AdjList(connections_1)
    start = stations_1[171]
    end = stations_1[219]

    astar_algo = Astar(adjList, stations_1, start, end)
    path_gen = PathGenerator()
    edgeTo, _ = astar_algo.findShortestPath()

    paths = path_gen.generatePath(edgeTo, start, end, connections_1)

    stations_in_path = set()
    for c in path_gen.pickTopInitinerary().connections:
        stations_in_path.add(c.s1.id)
        stations_in_path.add(c.s2.id)

    assert stations_in_path == {197, 151, 60, 126, 48, 250}


def main():
    pass


if __name__ == "__main__":
    main()


'''
    

'''