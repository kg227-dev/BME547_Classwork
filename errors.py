def divide_numbers(a, b):
    # creates an error
    try:
        return a/b
    except ZeroDivisionError:
        return "No can do: you divided by zero"


def main():
    print(divide_numbers(4, 0))


if __name__ == "__main__":
    main()
