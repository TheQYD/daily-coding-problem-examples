#!/usr/bin/python

def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def intesection(a, b):
    m = length(a)
    n = legnth(b)

    current_a = a
    current_b = b

    if m > n:
        for _ in range(m - n):
            current_a = current_a.next

    else:
        for _ in range(n - m):
            current_b = current_b.next

    while current_a != current_b:
        current_a = current_a.next
        current_b = current_b.next

    return current_a
