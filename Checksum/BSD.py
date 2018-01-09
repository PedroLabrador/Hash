# -*- coding: utf-8 -*-

# 16-bit BSD Checksum from file

def BSD(path):
    checksum = 0
    try:
        with open(path, 'r') as file:
            while True:
                ch = file.read(1)
                if not ch: break
                checksum = (checksum >> 1) + ((checksum & 0xFFFF) << 15)
                checksum += ord(ch)
                checksum &= 0xffff
            return hex(checksum)[2:].upper()
    except (Exception):
        return ''

if __name__ == '__main__':
    print (BSD(str(input('Path to the test file: '))))
