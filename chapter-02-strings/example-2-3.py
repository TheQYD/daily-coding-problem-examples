#!/usr/bin/python

def get_spaces(row, descending, lines):
    max_spaces = (lines - 1) * 2 - 1

    if descending == True:
        spaces = max_spaces - row * 2

    else:
        spaces = max_spaces - (lines - 1 - row) * 2

    return spaces

def is_descending(index, lines):

    return index % (2 * (lines - 1)) < lines - 1

def zigzag(sentence, lines):
    sentence_length = len(sentence)

    for row in range(lines):
        i = row
        line = [" " for _ in range(sentence_length)]

        while i < sentence_length:
            line[i] = sentence[i]
            descending = is_descending(i, lines)
            spaces = get_spaces(row, descending, lines)
            i += spaces + 1

        print("".join(line))

if __name__ == "__main__":

    sentence = "thisisazigzag"
    lines = 4
    zigzag(sentence, lines)
