#!/usr/bin/python

def max_circular_subarray(array):
    max_subarray_sum_wraparound = sum(array) - min_subarray_sum(array)

    return max(max_subarray_sum(array), max_subarray_sum_wraparound)

def max_subarray_sum(array):
    max_ending_here = 0
    max_so_far = 0

    for x in array:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def min_subarray_sum(array):
    min_ending_here = 0
    min_so_far = 0

    for x in array:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

if __name__ == "__main__":

    array = [1,2,3,4,5]
    print max_circular_subarray(array)
