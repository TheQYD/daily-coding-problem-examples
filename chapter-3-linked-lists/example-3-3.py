#!/usr/bin/python

def alternate(linkedlist):

    even = True
    current = linkedlist

    while current.next == True:

        if current.data > current.next.data and even:
            current.data, current.next.data = current.next.data, current.data

        elif current.data < current.next.data and not even:
            current.data, current.next.data = current.next.data, current.data

        even = not even
        current = current.next

    return linkedlist
