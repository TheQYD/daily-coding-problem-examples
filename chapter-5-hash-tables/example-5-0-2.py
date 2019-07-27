#!/usr/bin/python

def two_sum(lst, k):
    seen = {}
    for num in lst:
        if k - num in seen:
            return True
        seen[num] = True
    return False

if __name__ == "__main__":

    lst = [10, 15, 3, 7]
    k = 17

    print(two_sum(lst, k))
