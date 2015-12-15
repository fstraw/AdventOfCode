# -*- coding: utf-8 -*-
"""
Advent of Code - Day 8

@author: B. Batt
"""

import re


txt_file = open('INPUT.txt', 'rb')
inst = [r'{}'.format(l.replace('\n', '').replace('\r', '')) 
        for l in txt_file.readlines()]

def length_diff(string):
    hex_pattern = re.compile(r'(\\x[0-9a-hA-H]{2})')
    double_b = re.compile(r'(\\\\)')
    single_b = re.compile(r'(\\\")')
    hex_match = re.findall(hex_pattern, string)
    double_match = re.findall(double_b, string)
    single_match = re.findall(single_b, string)
    s = string
    num_quotes = 2 #account for containing string quotes
    if not s:
        return num_quotes
    for hexcode in hex_match:        
        s = s.replace(hexcode, '#')
    for double in double_match:
        s = s.replace(double, '#')
    for single in single_match:
        s = s.replace(single, '#')
    code_length = len(string)
    string_length = len(s) - num_quotes
    return s, code_length, string_length

def encoded_diff(string):
    hex_pattern = re.compile(r'(\\x[0-9a-hA-H]{2})')
    bs = re.compile(r'(\\)')
    dq = re.compile(r'(["])')
    bs_match = re.findall(bs, string)
    hex_match = re.findall(hex_pattern, string)
    dq_match = re.findall(dq, string)
    s = string
    num_quotes = 2 #account for containing string quotes
    if not s:
        return num_quotes
    for dq in dq_match:
        s = s.replace(dq, r'##')
    for hexcode in hex_match:        
        s = s.replace(hexcode, '#####')
    for bs in bs_match:
        s = s.replace(bs, r'##')
    old_string = len(string)
    new_string = len(s) + num_quotes
    return s, old_string, new_string

def part1():
    cl = 0
    sl = 0
    for s in inst:
        p = length_diff(s)
        cl += p[1]
        sl += p[2]
    result = cl - sl
    return result

def part2():
    old_string = 0
    new_string = 0
    for s in inst:
        p = encoded_diff(s)
        print p
        old_string += p[1]
        new_string += p[2]
    result = new_string - old_string
    return result

if __name__ == '__main__':
    print part1()
    print part2()  