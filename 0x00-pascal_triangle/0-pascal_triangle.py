#!/usr/bin/python3
""" pascal trinangle """


def pascal_triangle(n):
    """ function for pascal trinagel """
    triangle = []
    if (n <= 0):
        return []
    else:
        for i in range(n):
            temp_triangle = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_triangle.append(1)
                else:
                    temp_triangle.append(triangle[i - 1][j - 1] +
                                         triangle[i-1][j])
            triangle.append(temp_triangle)
        return triangle
