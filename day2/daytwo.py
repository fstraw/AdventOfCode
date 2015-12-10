# -*- coding: utf-8 -*-
"""
Advent of Code - Day 2

@author: B. Batt
"""


def parse_dimensions(dimensions):
    dims = open(dimensions).readlines()
    result = [map(int, dim.rstrip('\n').split('x')) for dim in dims]
    return result

def surface_area_single(box):
    l, w, h = box
    min_surf = min(((l * w), (w * h), (h * l)))
    sa = (2 * l * w) + (2 * w * h) + (2 * h * l)
    paper_needed = sa + min_surf
    return paper_needed

def ribbon_length(box):
    l, w, h = box
    volume = l * w * h
    perimeter = 2 * sum(sorted(box)[:2])
    result = volume + perimeter
    return result

if __name__ == '__main__':
    pass