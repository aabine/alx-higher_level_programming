#!/usr/bin/python3

if __name__ == "__main__":
    """print infinite addition of arguments"""
    import sys
    result = 0
    for i in range(len(sys.argv) - 1):
        cal = int(sys.argv[i + 1])
        result += cal
    print("{}".format(result))
