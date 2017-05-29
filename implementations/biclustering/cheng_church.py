import numpy as np


class MeanCachedMatrix:
    def __init__(self, nd_array):
        self.__array = nd_array

        self.rows_count, self.cols_count = self.__array.shape

        row_means = np.sum(nd_array, axis=1) / self.cols_count
        self.__row_means = {index: mean for index, mean in enumerate(row_means)}
        col_means = np.sum(nd_array, axis=0) / self.rows_count
        self.__column_means = {index: mean for index, mean in enumerate(col_means)}
        self._matrix_mean = sum(self.__row_means.values()) / self.rows_count

    def erase_row(self, row_index):
        self.__column_means = np.subtract(self.__column_means, (self.__array[row_index, :] / self.cols_count))
        dropped_row_mean = self.__row_means[row_index]
        old_rows_count = self.rows_count

        self.rows_count -= 1
        self.__row_means.pop(row_index)

        self._matrix_mean = ((self._matrix_mean - (dropped_row_mean / old_rows_count)) * old_rows_count / self.rows_count)

    def erase_column(self, column_index):
        self.__row_means -= self.__array[:, column_index] / self.cols_count
        dropped_col_mean = self.__column_means[column_index]
        old_cols_count = self.cols_count

        self.cols_count -= 1
        self.__column_means.pop(column_index)

        self._matrix_mean = ((self._matrix_mean - (dropped_col_mean / old_cols_count)) * old_cols_count / self.cols_count)

    # def add_column(self, column_index):
