#!/usr/bin/python

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0

class PrefixMapSum:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}

    def insert(self, key, value):

        value -= self.map.get(key, 0)
        self.map[key] = value
        
        trie = self._trie

        for char in key:
            if char not in trie.letters:
                trie.letters[char] = TrieNode()
            trie = trie.letters[char]
            trie.total += value


    def sum(self, prefix):
        d = self.trie

        for char in prefix:
            if char in d.letters:
                d = d.letters[char]
            else:
                return 0

        return d.total
