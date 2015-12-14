# -*- coding: utf-8 -*-
"""
Advent of Code - Day 7

@author: B. Batt
"""

calc = {}
results = {}

txt = ''
def parse_instructions(txt):
    strings = open(txt).readlines()
    instructions = [r.replace('\n', '') for r in strings]
    for inst in instructions:
        ops, val = inst.split('->')
        calc[val.strip()] = ops.strip().split(' ')

def evaluate_wire(wire):
    try:
        return int(wire)
    except ValueError:
        pass
    if wire not in results:
        ops = calc[wire]
        if len(ops) == 1:
            val = evaluate_wire(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              val = evaluate_wire(ops[0]) & evaluate_wire(ops[2])
            elif op == 'OR':
              val = evaluate_wire(ops[0]) | evaluate_wire(ops[2])
            elif op == 'NOT':
              val = ~ evaluate_wire(ops[1]) & 0xffff
            elif op == 'LSHIFT':
              val = evaluate_wire(ops[0]) << evaluate_wire(ops[2])
            elif op == 'RSHIFT':
              val = evaluate_wire(ops[0]) >> evaluate_wire(ops[2])
        results[wire] = val
    return results[wire]

if __name__ == '__main__':
    parse_instructions(txt)
    print 'Wire signal: {}'.format(evaluate_wire('a'))