#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    print(fib[:length])

print_fibonacci(9)
   