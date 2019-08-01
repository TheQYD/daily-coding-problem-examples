#/usr/bin/python

# This is an example on how to write a stack.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        # Add an item to the stack.
        self.stack.append(x)

    def pop(self):
        # Remove and return the top element.
        return self.stack.pop()

    def peek(self):
        # Return the top element.
        return self.stack[-1]
