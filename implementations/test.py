from biclustering.cheng_church import MeanCachedMatrix
import numpy as np

test_ndarray = np.arange(12).reshape(4, 3)

test_mcmatrix = MeanCachedMatrix(test_ndarray)
test_mcmatrix.erase_row(2)


# print((m_mean_f * np.multiply(*test_arr.shape) - row_means_f[2]) / np.multiply(*t_arr_drop.shape))