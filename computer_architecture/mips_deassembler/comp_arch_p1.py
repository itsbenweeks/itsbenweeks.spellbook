# -*- coding: utf-8 -*-
'''
Ben Weeks
CS472 Project 1
9/22/15
'''

from ctypes import c_short

opcodes = {
    0x4: 'beq',
    0x5: 'bne',
    0x23: 'lw',
    0x2b: 'sw'
}
functions = {
    0x20: 'add',
    0x22: 'sub',
    0x24: 'and',
    0x25: 'or'
}
instructions = [0x022DA822,
                0x8EF30018,
                0x12A70004,
                0x02689820,
                0xAD930018,
                0x02697824,
                0xAD8FFFF4,
                0x018C6020,
                0x02A4A825,
                0x158FFFF6,
                0x8E59FFF0
                ]

opcode_mask = 0b111111 << 26
src1reg_mask = 0b11111 << 21
src2reg_mask = 0b11111 << 16
destreg_mask = 0b11111 << 11
function_mask = 0b111111
offset_mask = 0xffff
pc = 0x7a060 - 4  # Subtract 4 to because we add before we print.

for i in instructions:
    pc += 4
    opcode = (i & opcode_mask) >> 26
    src1reg = (i & src1reg_mask) >> 21
    src2reg = (i & src2reg_mask) >> 16
    destreg = (i & destreg_mask) >> 11
    function = i & function_mask
    offset = c_short(i & offset_mask).value
    '''
    print """pc = {:x}
    opcode = {:x}
    src1reg = {}
    src2reg = {}
    destreg = {}
    function = {:x}
    offset ={}""".format(pc, opcode, src1reg, src2reg, destreg, function, offset)
    '''
    if not opcode:
        print "{:x} {} ${}, ${}, ${}".format(pc, functions[function], destreg, src1reg, src2reg)
    elif (opcodes[opcode] in ('bne', 'beq')):
        print "{:x} {} ${}, ${}, address {:x}".format(pc, opcodes[opcode], src1reg, src2reg, pc + offset * 4 + 4)
    else:
        print "{:x} {} ${}, {}(${})".format(pc, opcodes[opcode], src2reg, offset, src1reg)
