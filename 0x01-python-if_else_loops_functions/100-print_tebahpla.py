def print_reverse():
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{:c}".format(chr(i)), end="")
    print()