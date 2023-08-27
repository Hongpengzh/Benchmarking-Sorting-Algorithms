__author__ = 'Hongpeng Zhang'
__email__ = 'hongpeng.zhang@nmbu.no'

import numpy as np
import pandas as pd
import pickle

rng = np.random.default_rng(12235)
test_data_list = [rng.uniform(size=2**n) for n in range(17)]
test_data_avg = pd.Series(test_data_list, index= [f'test_data_2^{n}' for n in range(17)])
test_data_best = pd.Series(index= [f'test_data_2^{n}' for n in range(17)], dtype=object)
test_data_worst = pd.Series(index= [f'test_data_2^{n}' for n in range(17)], dtype=object)
for i in range(17):
    test_data_best[i] = np.sort(test_data_avg[i])
    test_data_worst[i] = np.sort(test_data_avg[i])[::-1]

with open('test_data.pkl', 'wb') as f:
    pickle.dump([test_data_avg, test_data_best, test_data_worst], f)