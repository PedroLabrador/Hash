# -*- coding: utf-8 -*-

space = 32
z = 122
a = 97
rotate = 13

def ROT13(string):
    output = ''
    data = string.lower()
    for i in data:
        current = ord(i)
        if (current == space):
            output += chr(space)
            continue 
        current = current + rotate
        if (current > z):
            dec = current - z
            current = a + dec - 1
        output += chr(current)
    return output
    
if (__name__ == '__main__'):
    print(ROT13(input('String: ')))
