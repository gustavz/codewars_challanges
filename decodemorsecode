#!/usr/bin/env python2
# -*- coding: utf-8 -*-
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    morseCode = ''
    ones = filter(None, bits.strip('0').split('0'))
    zeros = filter(None, bits.strip('0').split('1'))
    newbits = [None]*(len(ones)+len(zeros))
    newbits[::2] = ones
    newbits[1::2] = zeros
    
    dash = len(max(ones, key=len))
    dot = len(min(ones, key=len))
    pause_sm = dot*3
    pause_lg = dot*7
    null = dot*'0'
    
    newbits = filter(lambda x: x != null,newbits)
    
    for bit in newbits:
        if bit == dash*'1':
            morseCode += '-'
        elif bit == dot*'1':
            morseCode += '.'
        elif bit == pause_sm*'0':
            morseCode += ' '
        elif bit == pause_lg*'0':
            morseCode += '   '
            
    return morseCode
    
def decodeMorse(morseCode):
    decode = ''
    count = 1
    words = morseCode.strip().split('   ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            decode += MORSE_CODE[letter]
        if count < len(words):
            decode += ' '
        count += 1
    return decode
