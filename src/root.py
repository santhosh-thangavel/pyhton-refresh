#! usr/bin/env python3
import sys

def sqrt(x):
    guess =x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError as e:
        print(f'conversion error: --------> {e!r}', file=sys.stderr)
        raise


if __name__ == '__main__':
    main()
