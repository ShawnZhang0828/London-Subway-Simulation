import pytest
from subway.structures.connection import Connection
from subway.structures.line import Line
from subway.structures.station import Station
from subway.utils.dataLoader import DataLoader
from subway.utils.metricsHandler import MetricsHandler

file_paths_1 = ['_dataset/london.stations.csv', '_dataset/london.lines.csv', '_dataset/london.connections.csv']
file_paths_2 = ['_dataset/london.stations - Test.csv', '_dataset/london.lines - Test.csv', '_dataset/london.connections - Test.csv']

def test_loadData_2():
    global stations, lines, connections
    
    data_loader = DataLoader(file_paths_2[0], file_paths_2[1], file_paths_2[2])

    stations = data_loader.loadStation()
    lines = data_loader.loadLine()
    connections = data_loader.loadConnections(stations, lines)
    assert [station.lat for station in stations] == [51.5028, 51.5143, 51.5154, 51.5107, 51.5407, 51.5322, 51.5653, 51.6164, 51.4905]
    assert [line.name for line in lines] == ["Bakerloo Line", "Circle Line", "Hammersmith & City Line", "Jubilee Line", "Victoria Line"]
    assert [connection.time for connection in connections] == [3, 2, 3, 1, 1, 3, 1, 3, 2, 4, 1, 2, 1, 4, 3, 2, 3, 6, 4, 3]


def test_metrics_2():
    metrics_handler = MetricsHandler(stations, lines, connections)

    num_nodes = metrics_handler.computeNodeNum()
    num_edges = metrics_handler.computeEdgeNum()
    avg_deg = round(metrics_handler.computeAvgDeg(), 2)
    assert num_nodes == 9
    assert num_edges == 20
    assert avg_deg == 4.44

def test_dijkstra_2():
    pass

def test_astar_2():
    pass

def test_dijkstra_1():
    pass

def test_astar_1():
    pass


def main():
    pass


if __name__ == "__main__":
    main()


'''
    

'''