# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 10:36:08 2015

@author: bbatt
"""

import re
from collections import Counter


day5txt = 'day5.txt'
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

#def create_doubles_list(string):
#    double_list = []
#    for i in range(len(string)):
#        try:
#            double_list.append(string[i] + string[i+1])
#        except IndexError:
#            pass
#    return double_list

def create_doubles_list(string):
    return zip(string, string[1:])

def check_adjacent_doubles(dl):
    for i in range(len(dl)):
        try:
            if dl[i] == dl[i+1]:
                return False
        except IndexError:
            pass
    return True

def check_for_two_doubles(dl):        
#    check_list = [db for db, i in Counter(dl).items() if i > 1]
    repeats = []
    for i in range(len(dl)):
        try:
            if dl[i] == dl[i+1] and i <= len(dl):
                pass
            elif i == len(dl) and dl[i] in repeats:
                repeats.append(dl[i])
            else:
                repeats.append(dl[i])
        except IndexError:
            pass
    check_list = [db for db, i in Counter(repeats).items() if i > 1]    
    if len(check_list) > 0:
        return True
    else:
        return False

def check_for_splits(string):
    for i in range(len(string)):
        try:
            if string[i] == string[i+2]:
                if string[i] != string[i+1]:
                    return True
        except IndexError as e:
            print e.message
    return False
    
def better_nice(string):    
    dl = create_doubles_list(string)
    no_adjacent_doubles = check_adjacent_doubles(dl)
    two_or_more_doubles = check_for_two_doubles(dl)     
    ptwo = re.compile(r'([a-z])(?!\1)[a-z]\1')
    mtwo = ptwo.search(string)
#    splits = check_for_splits(string)
#    return dl
    if  two_or_more_doubles and no_adjacent_doubles and mtwo:
        print 'Two+ Doubles: {}'.format(two_or_more_doubles)
        print 'Splitz: {}'.format(mtwo)
        return 'Nice'
    else:
        print 'Two+ Doubles: {}'.format(two_or_more_doubles)
        print 'Splitz: {}'.format(mtwo)
        return 'Naughty'
        
if __name__ == '__main__':
    strings = parse_strings(day5txt)
    nice_count = 0
    sample = 'aaasxaa'
#    dl = create_doubles_list(sample)
#    print dl
    print check_for_two_doubles(sample)
#    print check_for_splits(sample)
#    print better_nice(sample)
#    for string in strings:
#        b = better_nice(string)
#        if b == 'Nice':
#            nice_count+=1
