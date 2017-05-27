from urllib import request
import numpy as np

# get data
url = "http://arep.med.harvard.edu/biclustering/lymphoma.matrix"
lines = request.urlopen(url).read().decode().strip().split('\n')
# insert a space before all negative signs
lines = list(' -'.join(line.split('-')).split(' ') for line in lines)
lines = list(list(int(i) for i in line if i) for line in lines)
data = np.array(lines)

generator = np.random.RandomState(0)
idx = np.where(data == 999)
data[idx] = generator.randint(-800, 801, len(idx[0]))

np.savez_compressed('lymphoma_mtx.npz', data)

