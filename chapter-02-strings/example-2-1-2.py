#!/usr/bin/python

from collections import defaultdict

def delete_if_zero(dictionary, character):

    if dictionary[character] == 0:
        del dictionary[character]

def anagram_indicies(word, string):

    result = []

    frequency = defaultdict(int)

    for character in word:
        frequency[character] += 1

    for character in string[:len(word)]:
        frequency[character] -= 1
        delete_if_zero(frequency, character)

    if not frequency:
        result.append(0)

    for i in range(len(word), len(string)):
        start_character = string[i - len(word)]
        end_character = string[i]
        delete_if_zero(frequency, start_character)

        frequency[end_character] -= 1
        delete_if_zero(frequency, end_character)

        if not frequency:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result

if __name__ == "__main__":

    word = "a cat leapt over the cat moon"
    string = "cat"

    print anagram_indicies(word, string)
