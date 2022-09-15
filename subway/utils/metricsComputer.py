def computeNodeNum(node_list):
    '''
        Compute the number of stations in the subway system
    '''
    return len(node_list)


def computeEdgeNum(edge_list):
    '''
        Compute the total number of connections in the subway system
    '''
    return len(edge_list)


def computeNodeDeg(node, edge_list):
    '''
        Compute the degree given a station (helper function for computeAvgDeg())
    '''
    count = 0

    for edge in edge_list:
        if node.id == edge.s1.id or node.id == edge.s2.id:
            count += 1

    return count

def computeAvgDeg(node_list, edge_list):
    '''
        Compute the average degree of all stations
    '''
    deg_sum = sum([computeNodeDeg(node, edge_list) for node in node_list])
    return deg_sum / computeNodeNum(node_list)