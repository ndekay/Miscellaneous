#!/usr/bin/env python


"""replaces vowels in a given string with substring 'inkle'."""


__author__ = "Nickolaus Dekay"
__version__ = "1.0"
__email__ = "nickolaus.dekay@gmail.com"


def main():
    name = input("What is your name? ")
    for x in range(len(name)):
        ch = name[x]
        if ch in ['a', 'e', 'i', 'o', 'u']:
            print("inkle", end="")
        else:
            print(ch, end="")
    print()


if __name__ == "__main__":
    main()
