#!/usr/bin/python

ENDS_HERE = '#'
words = ['dog', 'deer', 'deal']

class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie

        for char in text:
            if char not in trie:
                trie[char] = {}

            trie = trie[char]

        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie

        for char in prefix:
            if char in trie:
                trie = trie[char]

            else:
                return []

        return self._elements(trie)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']

            else:
                subresult = [c + s for s in self._elements(v)]

            result.extend(subresult)

        return result

trie = Trie()
for word in words:
    trie.insert(word)

def autocomplete(string):
    suffixes = trie.find(string)
    return [string + w for w in suffixes]
