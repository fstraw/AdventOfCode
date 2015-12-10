# -*- coding: utf-8 -*-
"""
Advent of Code - Day 3

@author: B. Batt
"""


def parse_directions(txt):
    directions = open(txt).readlines()[0]
    start = [0, 0]
    traveled_to = [[0, 0]]
    for direction in directions:
        if direction == '^':
            start[1]+=1
        elif direction == 'v':
            start[1]-=1
        elif direction == '>':
            start[0]+=1
        elif direction == '<':
            start[0]-=1
        val = (start[0], start[1])
        if not val in traveled_to:
            traveled_to.append(val)
    return traveled_to

def two_travelers(txt):
    directions = open(txt).readlines()[0]
    santa = True
    santa_start = [0, 0]
    robo_start = [0, 0]
    traveled_to = [(0, 0)]    
    for direction in directions:
        if santa == True:
            santa = False
            if direction == '^':
                santa_start[1]+=1
            elif direction == 'v':
                santa_start[1]-=1
            elif direction == '>':
                santa_start[0]+=1
            elif direction == '<':
                santa_start[0]-=1
            val = (santa_start[0], santa_start[1])
            if not val in traveled_to:
                traveled_to.append(val)
        elif santa == False:
            santa = True
            if direction == '^':
                robo_start[1]+=1
            elif direction == 'v':
                robo_start[1]-=1
            elif direction == '>':
                robo_start[0]+=1
            elif direction == '<':
                robo_start[0]-=1
            val = (robo_start[0], robo_start[1])
            if not val in traveled_to:
                traveled_to.append(val)
    result = len(traveled_to)
    return result

if __name__ == '__main__':
    pass
