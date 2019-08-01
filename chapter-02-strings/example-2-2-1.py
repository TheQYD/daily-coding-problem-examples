#!/usr/bin/python

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    result = []
    
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            
            if is_palindrome(word1 + word2) == True:
                result.append((i, j))
    
    return result

if __name__ == "__main__":
    
    array = ["code", "edoc", "da", "d"]
    print array
    print palindrome_pairs(array)
