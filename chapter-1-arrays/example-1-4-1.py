#!/usr/bin/python

# This program takes O(n^2) time. The example-1-4-2 is faster.

def smaller_elements(array):
    result = []

    for i, number in enumerate(array):
        count = sum(value < number for value in array[i + 1:])
        result.append(count)

    return result

if __name__ == "__main__":

    array = [3,4,9,6,1]
    print smaller_elements(array)
