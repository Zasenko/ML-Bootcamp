import sys


def assertionError(text):
    print(f"AssertionError: {text}")


def operations(a, b):
    print(f"Sum:        {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    if b == 0:
        print("Quotient:   ERROR (division by zero)")
        print("Remainder:  ERROR (modulo by zero)")
    else:
        print(f"Quotient:   {a / b}")
        print(f"Remainder:  {a % b}")


def main():
    """Usage: python operations.py <number1> <number2>\nExample:
        python operations.py 10 3"""
    count = len(sys.argv)
    if count > 3:
        assertionError("too many arguments")
    elif count == 1:
        print(main.__doc__)
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            operations(a, b)
        except ValueError:
            assertionError("only integers")


if __name__ == "__main__":
    main()
