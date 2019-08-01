#!/usr/bin/python

import heapq

def regular_numbers(n):
    solution = [1]
    last = 0
    count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x
            count += 1

            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)
