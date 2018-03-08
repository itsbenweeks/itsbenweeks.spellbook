#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ben Weeks
CS472 Project 3
11/22/15
'''

from stages import Pipeline

TEST_INSTRUCTIONS = {
    0x7A000: 0x00A63820,
    0x7A004: 0x8D0F0004,
    0x7A008: 0xAD09FFFC,
    0x7A00C: 0x00625022,
    0x7A010: 0x10C8FFFB,
    0x7A014: 0,
    0x7A018: 0,
    0x7A01C: 0,
    0x7A020: 0
}

INSTRUCTIONS = {
    0x7A000: 0xa1020000,
    0x7A004: 0x810afffc,
    0x7A008: 0x00831820,
    0x7A00C: 0x01263820,
    0x7A010: 0x01224820,
    0x7A014: 0x81180000,
    0x7A018: 0x81510010,
    0x7A01C: 0x00624022,
    0x7A020: 0,
    0x7A024: 0,
    0x7A028: 0,
    0x7A02C: 0,
    0x7A030: 0
}

pipeline = Pipeline()
i = 1
pc = 0x7A000
for key in INSTRUCTIONS.keys():
    title = "CYCLE {}".format(i)
    print "{:#^60}".format(title)
    pipeline.if_stage(INSTRUCTIONS, pc)
    pipeline.id_stage()
    pipeline.ex_stage()
    pipeline.mem_stage()
    pipeline.wb_stage()
    pipeline.print_out_everything()
    pipeline.copy_write_to_read()
    pc += 4
    i += 1

print "IT'S OVER!"
