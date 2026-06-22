import sys


def evenOdd(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def check_input(input):
    try:
        val = int(input)
        evenOdd(val)
    except ValueError:
        print("AssertionError: argument is not an integer")


def check_args():
    count = len(sys.argv)
    if count == 1:
        exit
    elif count > 2:
        print("AssertionError: more than one argument is provided")
    else:
        check_input(sys.argv[1])


check_args()
