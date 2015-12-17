# -*- coding: utf-8 -*-
"""
Advent of Code - Day 9

@author: B. Batt
"""

from itertools import permutations


txt_file = open('INPUT.txt', 'rb')
inst = [l.strip() for l in txt_file.readlines()]
locs_first = [i.split()[0] for i in inst]
locs_second = [i.split()[2] for i in inst]
locations = set(locs_first + locs_second)
possible_paths = [path for path in permutations(locations, len(locations))]
d = {i.split('=')[0].strip(): int(i.split('=')[1].strip()) for i in inst}
distances = []
for path in possible_paths:
    count = 0    
    path_distance = 0
    while count < len(path) - 1:
        from_loc = path[count]
        to_loc =  path[count + 1]
        try:                
            dist_to_next = d['{} to {}'.format(from_loc, to_loc)]
        except KeyError:
            dist_to_next = d['{} to {}'.format(to_loc, from_loc)]
        path_distance += dist_to_next
        count+=1
    distances.append(path_distance)

if __name__ == '__main__':
    print min(distances)
    print max(distances)