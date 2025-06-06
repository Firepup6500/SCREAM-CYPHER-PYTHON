# pylint: disable=missing-module-docstring,missing-function-docstring
from common import chars, alpha


def test():
    print(len(chars))
    for i, char in enumerate(chars):
        print(alpha[i] + ": " + char)


def encode(string: str) -> str:
    newString = ""
    for char in string:
        if char in alpha:
            newString += chars[alpha.index(char)]
        else:
            newString += char
    return newString


if __name__ == "__main__":
    print(encode(input("Input your string to encode: ")))
