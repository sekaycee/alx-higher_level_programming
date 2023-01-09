#!/usr/bin/python3
class MyInt(int):
    ''' inherit from class int '''
    def __eq__(self, other):
        ''' return != check '''
        return (int.__ne__(self, other))

    def __ne__(self, other):
        ''' return == check '''
        return (int.__eq__(self, other))
