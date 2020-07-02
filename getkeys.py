import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def keys_to_output(keys):
    # [J,K,L,I,N,E,P]
    output = [0,0,0,0,0,0,0,0]
    if 'J' in keys:
        output[0] = 1
    elif 'K' in keys:
        output[1] = 1
    elif 'L' in keys:
        output[2] = 1
    elif 'I' in keys:
        output[3] = 1
    elif 'N' in keys:
        output[4] = 1
    elif 'E' in keys:
        output[5] = 1
    elif 'P' in keys:
        output[6] = 1
    elif 'Z' in keys:
        output = [1,1,1,1,1,1,1,1]
    else:
        output[7] = 1

    return output