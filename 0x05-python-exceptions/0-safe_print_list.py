#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = count(my_list)
    except NotRealNumber:
        print("The number is not real ")
    else:
        print("{:d}.format(x)")
    finally:
        print(" ")
