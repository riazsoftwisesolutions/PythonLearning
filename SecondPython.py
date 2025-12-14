#!/usr/bin/env python3

def print_table(n: int, upto: int = 10) -> None:
    """Print multiplication table for `n` from 1 to `upto`."""
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")


if __name__ == "__main__":
    print("5-times table:")
    print_table(5)
    print()
    print("6-times table:")
    print_table(6)
    print()
    # Loop until user quits
    while True:
        user_input = input("Enter a number to see its multiplication table (or 'q' to quit): ").strip()
        if user_input.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        try:
            num = int(user_input)
            print_table(num)
            print()
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
