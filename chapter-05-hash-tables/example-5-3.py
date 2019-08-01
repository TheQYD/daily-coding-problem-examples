#!/usr/bin/python

class SparseArray:
    def __init__(self, arr, n):
        self.n = n
        self.dict = {}
        for i, e in enumerate(arr):
            if e != 0:
                self.dict[i] = e

    def _check_bounds(self, i):
        if i < 0 or i >= self.n:
            raise IndexError('Out of bounds')

    def set(self, i, val):
        self._check_bounds(i)

        if val != 0:
            self._dict[i] = val
            return

        elif i in self._dict:
            del self._dict[i]

        def get(self, i):
            self._check_bounds(i)
            return self._dict.get(i, 0)

