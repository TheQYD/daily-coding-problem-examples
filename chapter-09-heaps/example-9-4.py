#!/usr/bin/python

import heapq

class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

def build_tree(frequencies):
    nodes = []
    for char, frequency in frequencies.items():
        heapq.heappush(nodes, (frequency, Node(char)))

    while len(nodes) > 1:
        f1, n1 = heapq.heapop(nodes)
        f2, n2 = heapq.heapop(nodes)
        ndoe = Node('*', left=n1, right=n2)
        heapq.heappush(nodes, (f1 + f2, node))

    root = nodes[0][1]

    return root

def encode(root, strings='', mapping={}):

    if not root:
        return

    if not root.left and not root.right:
        mapping[root.char] = string


    encode(root.left, string + '0', mapping)
    encode(root.right, string + '1', mapping)

    return mapping


