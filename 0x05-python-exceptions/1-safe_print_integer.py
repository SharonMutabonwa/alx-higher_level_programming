#!/usr/bin/python3
def safe_print_integer(value):
    while True:
        try:
            print("{:d}".format(value))
            break
        except False:
            print("The value is not an integer")
    print()
    return(True)
