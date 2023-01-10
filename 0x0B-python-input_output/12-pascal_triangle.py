#!/usr/bin/python3
''' define a Pascal's Triangle module '''


def pascal_triangle(n):
    ''' represent Pascal's Triangle of size n
    Args:
        n: number of lines
    Returns:
        matrix: lists of integers representing the triangle
    '''
    if n <= 0:
        return ([])

    matrix = [[1]]
    while len(matrix) != n:
        tri = matrix[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        matrix.append(tmp)
    return (matrix)
