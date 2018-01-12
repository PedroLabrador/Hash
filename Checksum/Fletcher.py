# -*- coding: utf-8 -*-

def file_len(path):
    with open(path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def fletcher16(path):
    sum1 = 0
    sum2 = 0
    with open(path, 'r') as f:
        while True:        
            ch = f.read(1)
            if not ch: break
            sum1 = (sum1 + ord(ch)) % 255
            sum2 = (sum2 + sum1) % 255

        return hex((sum2 << 8) | sum1)[2:]

def fletcher32(path):
    sum1 = 0
    sum2 = 0

    flen = file_len(path)

    for i in range(flen):
        sum1 = sum2 = 0
        with open(path, 'r') as f:
            while True:
                ch = f.read(1)
                if not ch: break
                sum1 = sum1 + ord(ch)
                sum2 = sum2 + sum1
            sum1 = sum1 % 65535
            sum2 = sum2 % 65535

    with open (path, 'r') as f:
        while True:
            ch = f.read(1)
            if not ch: break
            sum1 = sum1 + ord(ch)
            sum2 = sum2 + sum1

    sum1 = sum1 % 65535
    sum2 = sum2 % 65535

    return hex((sum1 << 16) | sum2)[2:]


if __name__ == '__main__':
    print ('Option 1 fletcher16')
    print ('Option 2 fletcher32')
    opc = int(input('Option: '))
    if opc == 1:
        print(fletcher16('text.txt'))
    else:
        print(fletcher32('text.txt'))
