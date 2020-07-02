import numpy as np
import os
import cv2
from grab_screen import grab_screen
from getkeys import key_check, keys_to_output

file_name = 'training_data_1.npy'
if os.path.isfile(file_name):
    print('File exists, loading pervious data')
    training_data = list(np.load(file_name,allow_pickle=True))
else:
    print('File does not exist, starting fresh')
    training_data = []

def main():
    while True:
        screen = grab_screen(region=(0,70,700,470))
        screen_gray = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen_reshape = cv2.resize(screen_gray,(70,40))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen_reshape,output])

        if len(training_data)%5000 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

        if output != [1,1,1,1,1,1,1,1]:
            #print(key_check())
            print(output)
        else:
            np.save(file_name, training_data)
            break

main()