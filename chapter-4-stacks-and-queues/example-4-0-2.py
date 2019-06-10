#!/usr/bin/python

# This is an example on how to write a Queue.

from collections import deque

queue = deque()

queue.append(4)
queue.append(5)
queue.appendleft(6)

print(queue)

queue.popleft()
queue.pop()

print(queue)
