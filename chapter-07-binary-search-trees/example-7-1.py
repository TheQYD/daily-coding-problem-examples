#!/usr/bin/python

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def getbounds(root, x, floor=None, ceil=None):
        if not root:
            return floor, ceil

        if x == root.data:
            return x, x

        elif x < root.data:
            floor, ceil = get_bounds(root.left, x, floor, root.data)

        elif x > root.data:
            floor, ceil = get_bounds(root.right, x, root.data, ceil)

        return floor, ceil
