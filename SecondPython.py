#!/usr/bin/env python3

def print_table(n: int, upto: int = 10) -> None:
	"""Print multiplication table for `n` from 1 to `upto`."""
	for i in range(1, upto + 1):
		print(f"{n} x {i} = {n * i}")


if __name__ == "__main__":
	print_table(5)

