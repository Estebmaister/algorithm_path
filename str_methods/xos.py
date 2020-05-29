""" Return true if a string has the same amount of x's and o's """

import re


def xo(s):
    return len(re.findall("x", s, re.IGNORECASE)) == len(
        re.findall("o", s, re.IGNORECASE)
    )


def xo2(s):
    return True if s.lower().count("x") is s.lower().count("o") else False


def xo3(s):
    exes, ohs = (0, 0)
    for char in s.lower():
        if char == "x":
            exes += 1
        elif char == "o":
            ohs += 1
    return exes == ohs


print(xo("xxxxXOOomoo"))
