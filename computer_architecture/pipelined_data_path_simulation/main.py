#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ben Weeks
CS472 Project 3
11/22/15
'''

from stages import Pipeline

INSTRUCTIONS = {
    0x7A000: 0x00A63820,
    0x7A004: 0x8D0F0004,
    0x7A008: 0xAD09FFFC,
    0x7A00C: 0x00625022,
    0x7A010: 0x10C8FFFB,
    0x7A014: 0,
    0x7A018: 0,
    0x7A01c: 0,
    0x7A020: 0
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
    print "{:-^60}".format("Pre Copy")
    pipeline.print_out_everything()
    pipeline.copy_write_to_read()
    print "{:-^60}".format("Post Copy")
    pipeline.print_out_everything()
    pc += 4
    i += 1

print "IT'S OVER!"
