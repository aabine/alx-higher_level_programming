#!/usr/bin/python3

if __name__ == "__main__":
    """print arguments"""
    import sys
    print("{} arguments:".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        result = sys.argv[i]
        print("{}: {}".format(i, result))
