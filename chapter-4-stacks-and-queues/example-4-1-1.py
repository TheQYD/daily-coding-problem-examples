#!/usr/bin/python

# This example is the method I used to solve the problem.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def max(self):
        return max(self.stack)

if __name__ == "__main__":

    stack = Stack()
    print "appending 1"
    stack.push(1)
    print "appending 2"
    stack.push(2)
    print "appending 3"
    stack.push(3)

    # Should print 3
    print stack.max()
