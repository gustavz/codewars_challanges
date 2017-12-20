#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:58:38 2017

@author: nvidia
"""
"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones 
-- everytime you press the button it sends you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your starting point. 
Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's standing still!).
"""

def isValidWalk(walk):
    nn=ns=nw=ne = 0
    for i in walk:
        if i == "n":
            nn += 1
        elif i == "s":
            ns += 1
        elif i == "w":
            nw += 1
        elif i == "e":
            ne += 1
    if nn == ns and nw == ne and len(walk) == 10:
        return True
    else:
        return False