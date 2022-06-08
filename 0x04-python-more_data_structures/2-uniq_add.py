#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    info: adds all unique integers in a list (only once for each integer).
    '''
    result = 0
    for i in set(my_List):
        result += i
    return result
