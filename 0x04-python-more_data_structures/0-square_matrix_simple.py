#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_mat[len(new_mat):] = [[ele ** 2 for ele in i]]
    return new_mat
