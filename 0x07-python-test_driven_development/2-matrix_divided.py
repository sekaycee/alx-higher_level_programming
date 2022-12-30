#!/usr/bin/python3
"""
Define fuxnction that divide the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ divide the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_t = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_t)

    el_len = 0
    msg_s = "Each row of the matrix must have the same size"
    for el in matrix:
        if not el or not isinstance(el, list):
            raise TypeError(msg_t)

        if el_len != 0 and len(el) != el_len:
            raise TypeError(msg_s)

        for num in el:
            if not type(num) in (int, float):
                raise TypeError(msg_t)

        el_len = len(el)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
