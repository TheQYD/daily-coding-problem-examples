#!/usr/bin/python

def max_subarray_sum(array):

    current_max = 0

    for i in range(len(array) - 1):

        for j in range(i, len(array)):
            current_max = max(current_max, sum(array[i:j]))

        return current_max

if __name__ == "__main__":

    array = [34, -50, 42, 14, -5, 86]
    print max_subarray_sum(array)
