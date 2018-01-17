# -*- coding: utf-8 -*-

def roman(number):
    num = number
    decimalValue = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    romanNumeral = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]

    romanized = '';

    for i in range(len(decimalValue)):
        while decimalValue[i] <= num:
            romanized += romanNumeral[i]
            num -= decimalValue[i]

    return romanized


print(roman(int(input('Number: '))))
