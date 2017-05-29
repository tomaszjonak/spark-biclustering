import unittest
import numpy as np
from .context import cheng_church


class TestMeanCountingArray(unittest.TestCase):
    def setUp(self):
        self.base_array = np.arange(12).reshape(4, 3)
        self.matrix = cheng_church.MeanCachedMatrix(self.base_array)

    def test_mean(self):
        matrix_mean = self.matrix._matrix_mean
        valid_mean = np.sum(self.base_array) / np.multiply(*self.base_array.shape)
        self.assertEqual(matrix_mean, valid_mean)

    def test_validate_deleted_row_mean(self):
        row_index = 2
        dropped_array = np.delete(self.base_array, row_index, axis=0)
        valid_mean = np.sum(dropped_array) / np.multiply(*dropped_array.shape)
        self.matrix.erase_row(row_index)
        self.assertEqual(valid_mean, self.matrix._matrix_mean)

    def test_validate_deleted_column_mean(self):
        row_index = 1
        dropped_array = np.delete(self.base_array, row_index, axis=1)
        valid_mean = np.sum(dropped_array) / np.multiply(*dropped_array.shape)
        self.matrix.erase_column(row_index)
        self.assertEqual(valid_mean, self.matrix._matrix_mean)