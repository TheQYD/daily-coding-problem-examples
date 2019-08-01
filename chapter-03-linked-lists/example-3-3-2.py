#!/usr/bin/python

def alternate(linkedlist):

    previous = linkedlist
    current = linkedlist.next

    while current:
        if previous.data > current.data:
            previous.data, current.data = current.data , previous.data

        if not current.next:
            break

        if current.next.data > current.data:
            current.next.data, current.data = current.data, current.next.data

        previous = current.next
        current = current.next.next

    return linkedlist
