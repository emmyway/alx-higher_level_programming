#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if (len(argv) >= 2):
        s = "s"
        col = ":"
    else:
        s = ""
        col = "."
    print("{} argument{}{}".format(len(argv) - 1, s, col))
    for i, args in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, args))
