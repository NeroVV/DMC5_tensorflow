from Alexnet import alexnet2
from grab_screen import grab_screen
from directkeys import PressKey,ReleaseKey,J,K,L,I,N,E,P
from getkeys import key_check
import numpy as np
import time
import cv2

WIDTH = 70
HEIGHT = 40
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'model_DMC5/DMC5-{}-{}-epochs.model'.format(LR, 'alexnetv2')


GUN = np.argmax([1,0,0,0,0,0,0,0])
JUMP = np.argmax([0,1,0,0,0,0,0,0])
DEVIL_BREAK = np.argmax([0,0,1,0,0,0,0,0])
SWORD = np.argmax([0,0,0,1,0,0,0,0])
DEVIL_TRIGGER = np.argmax([0,0,0,0,1,0,0,0])
THROW = np.argmax([0,0,0,0,0,1,0,0])
LOCK = np.argmax([0,0,0,0,0,0,1,0])
NO_CHOICE = np.argmax([0,0,0,0,0,0,0,1])

t_time = 0.1

def jump():
    PressKey(K)
    time.sleep(t_time)
    ReleaseKey(K)

def sword():
    PressKey(I)
    time.sleep(0.3)
    ReleaseKey(I)
    time.sleep(0.3)

def gun():
    PressKey(J)
    time.sleep(2)
    ReleaseKey(J)

def devil_break():
    PressKey(L)
    time.sleep(t_time)
    ReleaseKey(L)
    ReleaseKey(P)

def lock():
    PressKey(P)
    time.sleep(t_time)


def devil_trigger():
    PressKey(N)
    time.sleep(t_time)
    ReleaseKey(N)

def throw():
    PressKey(E)
    time.sleep(t_time)
    ReleaseKey(E)
    ReleaseKey(P)

model = alexnet2(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        screen = grab_screen(region=(0,70,700,470))
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen,(70,40))
        print('Frame took {} seconds'.format(time.time()-last_time))

        last_time = time.time()
        prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
        print(prediction)
        action = np.argmax(prediction)
        print('模型的预测:{}'.format(action))
        if action == GUN:
            print('枪')
            gun()
        elif action == JUMP:
            print('跳')
            jump()
        elif action == DEVIL_BREAK:
            print('机械臂')
            devil_break()
        elif action == DEVIL_TRIGGER:
            print('魔化')
            devil_trigger()
        elif action == SWORD:
            print('剑')
            sword()
        elif action == THROW:
            print('投技')
            throw()
        elif action == LOCK:
            print('锁定')
            lock()
        elif action == NO_CHOICE:
            print('无')

        keys = key_check()
        if 'T' in keys:
            time.sleep(1)
            break

main()