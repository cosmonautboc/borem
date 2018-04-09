# -*- coding: utf-8 -*-

import numpy as np

def create_data(samples, timesteps, win_len):
    x_data = np.random.uniform(0, 1, (samples, timesteps))
    index = np.arange(samples)
    np.random.shuffle(index)
    ok_index = index[:int(samples/2)]
    ng_index = index[int(samples/2):]
    x_data[ok_index, 0] = 1
    x_data[ng_index, 0] = 0
    y_data = x_data[:, 0].copy()

    # create seqential data
    seq_num = timesteps - win_len + 1
    x_seq = np.array([x[i:i+win_len] for x in x_data for i in np.arange(seq_num)])
    y_seq = y_data.repeat(seq_num)

    # create stateful data
    x_stateful = x_data.copy()
    y_stateful = y_data[np.newaxis, :].T.repeat(timesteps, axis=1)

    # print(x_data.shape)
    # print(y_data.shape)
    # print(x_data)
    # print(y_data)

    # print(x_seq.shape)
    # print(y_seq.shape)
    # print(x_seq)
    # print(y_seq)

    # print(x_stateful.shape)
    # print(y_stateful.shape)
    # print(x_stateful)
    # print(y_stateful)

    return x_seq, y_seq, x_stateful, y_stateful


if __name__=='__main__':
    create_data(10, 8, 3)
