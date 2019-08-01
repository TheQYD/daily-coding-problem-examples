#!/usr/bin/python

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    dictionary = {}

    for i, word in enumerate(words):
        dictionary[word] = i

    result = []

    for i, word in enumerate(words):
        for character_i in range(len(words)):

            prefix = word[:character_i]
            suffix = word[character_i:]

            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if (is_palindrome(suffix) and reversed_prefix in dictionary):
                if i != dictionary[reversed_prefix]:
                    result.append((i, dictionary[reversed_prefix]))

            if (is_palindrome(prefix) and reversed_suffix in dictionary):
                if i != dictionary[reversed_suffix]:
                    result.append((dictionary[reversed_suffix, i]))

    return result
