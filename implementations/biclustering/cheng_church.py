import numpy as np


def calculate_means(matrix):
    row_means = np.sum(matrix, axis=1) / matrix.shape[1]
    col_means = np.sum(matrix, axis=0) / matrix.shape[0]
    matrix_mean = np.sum(row_means) / matrix.shape[0]
    return matrix_mean, row_means, col_means


class BiclusteringProblem:
    def __init__(self, matrix):
        self._matrix = matrix
        self.I = list(range(matrix.shape[0]))
        self.J = list(range(matrix.shape[1]))

    def _calculate_i_mean(self, i):
        return np.sum(self._matrix[i, self.J]) / self._matrix.shape[0]

    def _calculate_j_mean(self, j):
        return np.sum(self._matrix[self.I, j]) / self._matrix.shape[1]

    def _calculate_matrix_mean(self):
        return np.sum(self._matrix) / np.multiply(*self._matrix.shape)

    def _calculate_di(self, i):

        return

    def _calculate_dj(self, j):

    def solve(self):
