#!/usr/bin/python

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root.data == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    elif root.data == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    elif root.data == TIMES:
        return evaluate(root.left) * evaluate(root.right)
    elif root.data == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val

