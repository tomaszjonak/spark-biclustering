import sys
import csv
import numpy as np

matrix = []
with open(sys.argv[1], 'r') as fd:
    print('>>> File loaded')
    reader = csv.reader(fd, delimiter='\t')
    count = 0
    while "dataset_table_begin" not in next(reader)[0]:
        count += 1
    print('>>> Data front found at {} (zero counted), printing headers'.format(count))
    line = next(reader)
    print(line)
    line = next(reader)
    while "dataset_table_end" not in line[0]:
        matrix.append(line[2:-20])
        line = next(reader)
    print('>>> Matrix truncated')

matrix = np.array(matrix).astype(np.float)
print('>>> Matrix contents peek')
print(matrix)

dest_file = sys.argv[2]
# with open(dest_file, 'w') as dest_fd:
np.savez_compressed(dest_file, matrix)
print('>>> File saved ({})'.format(dest_file))

