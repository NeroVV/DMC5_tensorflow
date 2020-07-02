import numpy as np
import os

file_name_1 = 'training_data_1.npy'
file_name_2 = 'training_data_2.npy'
file_name = 'training_data.npy'

if os.path.isfile(file_name_1):
    print("file exists , loading previous data")
    training_data_1 = list(np.load(file_name_1,allow_pickle=True))

if os.path.isfile(file_name_2):
    print("file exists , loading previous data")
    training_data_2 = list(np.load(file_name_2,allow_pickle=True))

final_data = training_data_1+training_data_2
print(len(final_data))
np.save(file_name,final_data)