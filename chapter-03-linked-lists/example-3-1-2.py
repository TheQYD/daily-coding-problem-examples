#!/usr/bin/python

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def reverse(head):
    prev = None
    current = head

    while current is not None:

        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev

if __name__ == "__main__":

    data = [1,2,3,4,5]
    node = Node(data, None, None)
    print reverse(node)
