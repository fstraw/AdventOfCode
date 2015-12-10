# -*- coding: utf-8 -*-
"""
Advent of Code - Day 4

@author: B. Batt
"""

import hashlib


def find_hash(string):
    m = hashlib.md5()    
    i = 0
    m.update(sample)
    while not m.hexdigest()[:6] == '000000':
        i += 1
        m = hashlib.md5()
        m.update(string + str(i))        
    return i, m.hexdigest()

if __name__ == '__main__':
    pass