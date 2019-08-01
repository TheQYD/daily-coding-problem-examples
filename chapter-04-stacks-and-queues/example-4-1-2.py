#!/usr/bin/python

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maximums = []

    def push(self, value):
        self.stack.append(value)
        
        if self.maximums:
            self.maximums.append(max(value, self.maximums[-1]))
        else:
            self.maximums.append(value)

    def pop(self):
        if self.maximums:
            self.maximums.pop()

        return self.stack.pop()

    def max(self):
        return self.maximums[-1]

if __name__ == "__main__":

    stack = MaxStack()

    stack.push(1)
    stack.push(4)
    stack.push(5)
    stack.push(2)

    print stack.max()
