#!/usr/bin/python

from collections import deque

# k is the maximum length of each subarray.
def max_of_subarrays(array, k):
    queue = deque()
    
    for i in range(k):    
        while queue and array[i] > array[queue[-1]]:
            queue.pop()
        
        queue.append(i)

    for i in range(k, len(array)):
        print array[queue[0]]

        while queue and queue[0] <= i - k:
            queue.popleft()

        while queue and array[i] >= array[queue[-1]]:
            queue.pop()

        queue.append(i)

    print array[queue[0]]

if __name__ == "__main__":

    array = [10, 5, 2, 7, 8, 7]
    max_of_subarray(array, k)
