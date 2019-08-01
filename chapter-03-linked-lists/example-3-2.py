#!/usr/bin/python

def add(node0, node1, carry=0):
    if not node0 and not node1 and not carry:
        return None

    node0_val = node0.data if node0 else 0
    node1_val = node1.data if node1 else 0
    total = node0_val + node1_val + carry

    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total >= 10 else 0

    return Node(total % 10, add(node0_next, node1_next, carry_next))
