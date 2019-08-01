#!/usr/bin/python

import bisect

def smaller_elements(array):

    result = []
    seen = []

    for number in reversed(array):

        i = bisect.bisect_left(seen, number)
        result.append(i)
        bisect.insort(seen, number)

    return list(reversed(result))

if __name__ == "__main__":

    array = [3,4,9,6,1]
    print smaller_elements(array)
