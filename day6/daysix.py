# -*- coding: utf-8 -*-
"""
Advent of Code - Day 6

@author: B. Batt
"""

def create_grid(size):
    grid = [[0 for i in range(size)] for x in range(size)]
    return grid

def parse_instructions(txt):
    strings = open(txt).readlines()
    raw = [r.replace('\n', '') for r in strings]
    instructions = []
    for i in raw:
        start = (int(i.split()[-3].split(',')[0]), 
                 int(i.split()[-3].split(',')[1]))
        end = (int(i.split()[-1].split(',')[0]), 
               int(i.split()[-1].split(',')[1]))
        if i.startswith('turn off'):
            instructions.append((start, end, 'turn off'))
        elif i.startswith('turn on'):
            instructions.append((start, end, 'turn on'))
        elif i.startswith('toggle'):            
            instructions.append((start, end, 'toggle'))
    return instructions

def select_cells(grid, start, end, op):
    for row in range(start[1], end[1]+1):
        for column in range(start[0], end[0]+1):
            if op == 'turn off':
                grid[row][column] = 0
            elif op == 'turn on':
                grid[row][column] = 1
            elif op == 'toggle':
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0

def adjust_brightness(grid, start, end, op):
    for row in range(start[1], end[1]+1):
        for column in range(start[0], end[0]+1):
            if op == 'turn off':
                if grid[row][column] > 0: 
                    grid[row][column] -= 1
            elif op == 'turn on':
                grid[row][column] += 1
            elif op == 'toggle':
                grid[row][column] += 2

def part1():
    grid = create_grid(1000)
    instructions = parse_instructions(txt)
    for i in instructions:
        start, end, op = i
        select_cells(grid, start, end, op)
    lights_on = 0
    for row in grid:
        for cell in row:
            if cell == 1:
                lights_on+=1
    print lights_on
    
def part2():
    grid = create_grid(1000)
    instructions = parse_instructions(txt)
    for i in instructions:
        start, end, op = i
        adjust_brightness(grid, start, end, op)
    total_brightness = 0
    for row in grid:
        for cell in row:
            total_brightness += cell
    print total_brightness
    
if __name__ == '__main__':
    part1()
    part2()