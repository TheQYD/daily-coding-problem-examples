#!/usr/bin/python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse(node):
    
    head, _ = _reverse(node)
    return head

def _reverse(node):
    if node is None:
        return None, None

    if node.next is None:
        return node, node

    head, tail = _reverse(node.next)
    node.next = None
    tail.next = node
    return head, node

if __name__ == "__main__":

    data = [1,2,3,4,5]
    node = Node(data, None)
    print reverse(node)
