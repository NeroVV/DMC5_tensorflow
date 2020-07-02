import numpy as np
from random import shuffle


train_data = np.load('training_data.npy',allow_pickle=True)

# [J,K,L,I,N,E,P]
gun = []
jump = []
devil_breaker = []
sword = []
devil_trigger = []
throw = []
lock = []
no_choice = []

shuffle(train_data)

print(len(train_data))
for data in train_data:
    img = data[0]
    choice = data[1]

    if choice[0] == 1:
        gun.append([img,choice])

    elif choice[1] == 1:
        jump.append([img,choice])

    elif choice[2] == 1:
        devil_breaker.append([img,choice])

    elif choice[3] == 1:
        sword.append([img,choice])

    elif choice[4] == 1:
        devil_trigger.append([img,choice])

    elif choice[5] == 1:
        throw.append([img,choice])

    elif choice[6] == 1:
        lock.append([img,choice])

    elif choice[7] == 1:
        no_choice.append([img,choice])
'''
print('*'*100)
print(len(train_data))
print('*'*100)
print(len(gun))
print(len(jump))
print(len(devil_breaker))
print('*'*100)
print(len(sword))
print(len(devil_trigger))
print(len(throw))
print(len(lock))
print('*'*100)
print(len(no_choice))
'''

no_choice = no_choice[:len(sword)]
final_data =gun + jump + devil_breaker + sword + devil_trigger + throw + lock + no_choice
shuffle(final_data)
print(len(final_data))
np.save('training_data_balance.npy', train_data)
