#!/usr/bin/python

from collections import Counter

def is_anagram(s1, s2):

    return Counter(s1) == Counter(s2)

def anagram_indicies(word, string):
    result = []
    
    for i in range(len(string) - len(word) + 1):
        window = string[i:i + len(word)]
        
        if is_anagram(window, word) == True:
            result.append(i)

    return result

if __name__ == "__main__":
    
    word = "ab"
    string = "abxabaxxabaxa"
    print anagram_indicies(word, string)
