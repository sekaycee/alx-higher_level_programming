#!/usr/bin/python3
''' create a class MyList derived from list '''


class MyList(list):
    ''' inherit the attributes references of class list
    Args:
        list: class list
    '''
    def print_sorted(self):
        ''' print the sorted list '''
        print(sorted(self))
