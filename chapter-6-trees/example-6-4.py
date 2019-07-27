#!/usr/bin/python

from collections import defaultdict, deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def smallest_level(root):
    queue = deque([])
    queue.append((root, 0))

    level_to_sum = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_to_sum[level] += node.data

        if node.right:
            queue.append((node.right, level + 1))

        if node.left:
            queue.append((node.left, level + 1))

    return min(level_to_sum, key=level_to_sum.get)
