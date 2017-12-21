#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. 
Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

"""

def is_isogram(string):
    if string:
        from collections import Counter
        counter = Counter(string.lower())
        if max(counter.values()) == 1:
            return True
        return False
    else:
        return True
    