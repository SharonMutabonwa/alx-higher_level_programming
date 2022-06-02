#!/usr/bin/python3
if __name == "__main__":
    from calculator_1.py import add, sub, mul, div

    a = 10
    b = 5

print("{} + {} = {}".formate(a, b, add(a, b)))
print("{} + {} = {}".formate(a, b, sub(a, b)))
print("{} + {} = {}".formate(a, b, mul(a, b)))
print("{} + {} = {}".formate(a, b, div(a, b)))
