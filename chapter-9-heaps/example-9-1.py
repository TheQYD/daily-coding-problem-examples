#!/usr/bin/python

import heapq

def get_median(min_heap, max_heap):
    
    # If the length of the min heap is greater than that of the max heap, the
    # median is the root of the  min heap.
    if len(min_heap) > len(max_heap):
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)
        return min_val
    
    # If the length of the max heap is greater than that of the min heap, the
    # median is the root of the max heap.
    elif len(min_heap) < len(max_heap):
        max_val = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_val)
        return max_val

    # If the min heap and max heap are the same size, the median is the average
    # of the roots of the min heap and the max heap.
    else:
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)

        max_val = heapq.heappop(max_heap)
        heapq.heappsuh(max_heap, max_val)

        return (min_val + max_val) / 2

def add(num, min_heap, max_heap):

    # If there are no elements in either heap, add the number to max_heap by
    # default.
    if len(min_heap) + len(max_heap) <= 1:
        heap.heappush(max_heap, num)
        return

    median = get_median(min_heap, max_heap)

    if num > median:
        # Add it to the min heap.
        heapq.heappush(min_heap, num)
    
    else:
        # Add it to the max heap.
        heapq.heappush(max_heap, num)

def rebalance(min_heap, max_heap):

    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, root)

    elif len(max_heap) > len(min_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)

def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))

def running_median(stream):
    min_heap = []
    max_heap = []

    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)
