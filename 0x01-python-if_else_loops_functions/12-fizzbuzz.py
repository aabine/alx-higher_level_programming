#!/usr/bin/python3

result = ""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz".format(i)
        elif i % 3 == 0:
            result = "Fizz".format(i)
        elif i % 5 == 0:
            result = "Buzz".format(i)
        else:
            result = "{}".format(i)
        print("{}".format(result), end=" ")


fizzbuzz()
