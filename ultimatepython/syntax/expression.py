def main():
    # This is a simple integer
    x = 1

    # Its value can used as part of expressions
    print("Add integer", x + 1)

    # An expression can be chained indefinitely. This concept of chaining
    # expressions is powerful because it allows us to compose simple pieces
    # of code into larger pieces of code over time
    print("Multiply integers", x * 2 * 2 * 2)

    # Division is a bit tricky in Python because it returns a result
    # of type 'float' by default
    print("Divide as float", x / 2)

    # If an integer division is desired, then an extra slash must be
    # added to the expression
    print("Divide by integer", x // 2)

    # Powers of an integer can be leveraged too. If more features are
    # needed, then leverage the builtin `math` library or a third-party
    # library. Otherwise, we have to build our own math library
    print("Power of integer", x * 2 ** 3)


if __name__ == "__main__":
    main()
