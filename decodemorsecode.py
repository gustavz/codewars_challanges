#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
In this kata you have to write a Morse code decoder for wired electrical telegraph.

Electric telegraph is operated on a 2-wire line with a key that, when pressed, 
connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted 
as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.

However, the standard does not specify how long that "time unit" is.
 And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, 
 a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, 
and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. 
After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

    Function decodeBits(bits), that should find out the transmission rate of the message, 
    correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) 
    and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, 
    make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.

    Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

The Morse code table is preloaded for you as MORSE_CODE dictionary (MorseCode class for Java), feel free to use it.
"""
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
    
    if not zeros:
        return '.'
    
    dash = len(max(ones, key=len))
    dot = len(min(ones, key=len))
    pause_dots = len(min(zeros, key=len))
    pause_chars = dot*3
    pause_words = dot*7
    
    for bit in newbits:
        if bit == pause_chars*'0':
            morseCode += ' '
        elif bit == pause_words*'0':
            morseCode += '   '
        elif bit == pause_dots*'0':
            continue
        elif bit == dot*'1' and dot <= pause_dots:
            morseCode += '.'
        elif bit == dash*'1':
            morseCode += '-'
                       
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