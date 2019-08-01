#!/usr/bin/python

def get_best_word(string, k):
    string = list(string)

    if k == 1:
        best_word = string

        for i in range(1, len(string)):
            if string[i:] + string[:i] < best_word:
                best = string[i:] + string[:i]

        return "".join(best_word)

    else:

        return "".join(sorted(string))

if __name__ == "__main__":

    string = "ailyd"
    k = 2
    print get_best_word(string, k)
