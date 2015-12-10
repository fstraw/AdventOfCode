# -*- coding: utf-8 -*-
"""
Advent of Code - Day 5

@author: B. Batt
"""

##regex would be better (probably)


def parse_strings(txt):
    strings = open(txt).readlines()
    result = [r.replace('\n', '') for r in strings]
    return result

def nice(string):
    vowels = 'aeiou'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    doubles = [l*2 for l in letters]
    cannot_contain_list = ['ab', 'cd', 'pq', 'xy']
    vowel_count = 0
    double_count = 0
    cannot_contain_count = 0
    vowel_criteria = False
    letter_criteria = False
    cannot_contain_criteria = False
    ##test for vowels
    for letter in string:
        if letter in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        vowel_criteria = True    
    ##Test for double letters
    for double in doubles:
        if double in string:
            double_count += 1
    if double_count >= 1:
        letter_criteria = True
    #Test for invalid strings
    for invalid in cannot_contain_list:
        if invalid in string:
            cannot_contain_count += 1
    if not cannot_contain_count > 0:
        cannot_contain_criteria = True       
    if (vowel_criteria == True and letter_criteria == 
        True and cannot_contain_criteria == True):
        return 'Nice'            

## kudos to Redditor u/OffensiveCanadian for this approach; 
##I only modified it slightly to suit my needs

def better_nice(strings):
    nice_strings = 0
    for l in strings:
        for i in range(len(l)-2):
            if l[i] == l[i+2]:
                break
        else:
            continue
        for i in range(len(l)-1):
            if l.count(l[i] + l[i+1]) > 1:
                nice_strings += 1
                break
        else:
            continue
    return nice_strings
        
if __name__ == '__main__':
    pass
