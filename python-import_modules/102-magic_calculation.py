#!/usr/bin/python3

from dis import dis


def magic_calculation(a, b):
    bytecode = dis(magic_calculation)
    for instr in bytecode:
        print(instr.opname)
