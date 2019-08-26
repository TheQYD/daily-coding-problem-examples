#!/usr/bin/python

from collections import defaultdict

def traverse(graph, current, result):
    descendants = 0

    for child in graph[current]:
        num_nodes, result = traverse(graph, child, result)

        result[child] += num_nodes - 1
        descendants += num_nodes

    return descendants + 1, result

def max_edges(graph):
    start = list(graph)[0]
    verticies = defaultdict(int)

    _, descendants = traverse(graph, start, verticies)

    return len([val for val in descendants.values() if val % 2 == 1])

if __name__ == "__main__":

    graph = {

        1: [2, 3],
        2: [],
        3: [4, 5],
        4: [6, 7, 8],
        5: [],
        6: [],
        7: [],
        8: []
    }

    print max_edges(graph)
