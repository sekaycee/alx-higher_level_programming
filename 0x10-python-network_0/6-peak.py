#!/usr/bin/python3
''' Define a peak-finding algorithm '''


def find_peak(list_of_integers):
    ''' Find a peak in a list of unsorted integers '''
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if list_of_integers[mid - 1] < peak > list_of_integers[mid + 1]:
        return peak
    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
