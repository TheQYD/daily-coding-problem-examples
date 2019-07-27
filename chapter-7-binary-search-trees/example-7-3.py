#!/usr/bin/python

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def make_trees(low, high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high + 1):
        left = make_trees(low, i - 1)
        right = make_trees(i + 1, high)

        for l in left:
            for r in right:
                node = Node(i, left=l, right=r)
                trees.append(node)

    return trees

def preorder(root):
    result = []

    if root:
        result.append(root.data)
        result += preorder(root.left)
        result += preorder(root.right)

    return result

def construct_trees(N):
    trees = make_trees(1, N)
    for tree in trees:
        print(preorder(tree))
