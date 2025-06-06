# pylint: disable=missing-module-docstring,missing-function-docstring,too-many-nested-blocks
from common import chars, alpha, validSymbols, thingsThatCountAsAnA, lower, fixup


def test():
    print(len(alpha))
    for i, char in enumerate(alpha):
        print(chars[i] + ": " + char)


def decode(string: str) -> str:
    newString = ""
    string = fixup(string)
    i = 0
    while i < len(string):
        char = string[i]
        if char in thingsThatCountAsAnA:
            if len(string) > i + 1:
                nextChar = string[i + 1]
                if nextChar in validSymbols:
                    if char + nextChar in chars:
                        i += 1
                        char = char + nextChar
                        if len(string) > i + 1:
                            nextNextChar = string[i + 1]
                            if nextNextChar == lower:
                                i += 1
                                char = char + lower
            newString += alpha[chars.index(char)]
        else:
            newString += char
        i += 1
    return newString


if __name__ == "__main__":
    print(decode(input("Input your string to decode: ")))
