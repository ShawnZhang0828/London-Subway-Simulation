import matplotlib.pyplot as plt
from subway.utils.metricsComputer import computeNodeDeg, computeNodeNum


def plot(stations, graphs):
    '''
        Plot the metrics using matplotlib
        x-axis: possible degrees
        y-axis: number of stations with the degree
    '''
    num_stations = computeNodeNum(stations)

    deg_dic = {}
    for i in range(num_stations):
        deg_of_node = computeNodeDeg(stations[i], graphs)
        if computeNodeDeg(stations[i], graphs) not in deg_dic.keys():
            deg_dic[deg_of_node] = 1
        else:
            deg_dic[deg_of_node] += 1

    plt.bar(deg_dic.keys(), deg_dic.values())
    plt.title("Distribution of Node's Degree")
    plt.xlabel('Degree')
    plt.ylabel('Number of Stations')
    plt.show()
