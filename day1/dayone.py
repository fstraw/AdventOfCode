# -*- coding: utf-8 -*-
"""
Advent of Code - Day 1

@author: B. Batt
"""


def go_to_floor(instructions):
    i = 0
    for index, step in enumerate(instructions):
        if step == '(':
            i+=1
        elif step == ')':
            i-=1
        if i == -1:
            return index + 1
    
if __name__ == '__main__':
    pass