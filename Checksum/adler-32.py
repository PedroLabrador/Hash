# -*- coding: utf-8 -*-

CONST_ADLER = 65521

def adler32(S):
    A = 1
    B = 0

    for i in S:
        A = (A + ord(i)) % CONST_ADLER
        B = (B + A) % CONST_ADLER

    return hex((B << 16) | A).upper()[2:]



if __name__ == '__main__':
    print (adler32(input('..: ')))
