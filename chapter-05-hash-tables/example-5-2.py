#!/usr/bin/python

from collections import defaultdict

def fewest_cuts(wall):
    cuts = defaultdict(int)


    for row in wall:
        length = 0
        for brick in row[:-1]:
            length += brick
            cuts[length] += 1

    return len(wall) - max(cuts.values())

