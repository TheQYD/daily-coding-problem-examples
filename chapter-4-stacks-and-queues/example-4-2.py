#!/usr/bin/python

def balance(string):
    stack = []

    for character in stack:
        if character in ["(", "[", "{"]:
            stack.append(character)

        else:
            if not stack:
                return False

        if (character == ")" and stack[-1] != "(") \
        or (character == "]" and stack[-1] != "[") \
        or (character == "}" and stack[-1] != "{"):
            return False
        
        stack.pop()

    return len(stack) == 0
