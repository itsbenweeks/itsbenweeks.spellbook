#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Benjamin Weeks
CS472 Project 1
September, 22nd, 2015
"""
MAIN_MEMORY = []
for x in xrange(2048):
    MAIN_MEMORY.append(x & 0xff)


class Slot(object):
    """
    A software implementation of a slot with a 16 byte block
    """
    def __init__(self):
        self.valid = 0
        self.tag = 0
        self.data = []
        for x in xrange(16):
            self.data.append(0)

    def __str__(self):
        result = "{0:^5X} {1:^3X}     ".format(self.valid, self.tag)
        for datum in self.data:
            result += "{:<3X}".format(datum)
        return result

    def check_hit(self, tag):
        return self.valid and (self.tag == tag)

    def read_slot(self, address):
        tag = (address & (0b111 << 8)) >> 8
        result = [MAIN_MEMORY[address]]
        if self.check_hit(tag):
            result.append("Cache Hit")
        else:
            for x in xrange(len(self.data)):
                self.data[x] = MAIN_MEMORY[(address >> 4 << 4) + x]
            self.tag = tag
            self.valid = 1
            result.append("Cache Miss")
        return result

    def write_slot(self, address, datum):
        tag = (address & (0b111 << 8)) >> 8
        if self.check_hit(tag):
            self.data[address & 0b1111] = datum
            MAIN_MEMORY[address] = datum
            return "Cache Hit"
        else:
            self.tag = tag
            return "Cache Miss"


class Cache(object):
    """
    A software implementation of a direct-mapped cache with 16 slots
    """
    def __init__(self):
        self.cache = []
        for x in xrange(16):
            self.cache.append(Slot())

    def __str__(self):
        result = "Slot Valid Tag     Data\n"
        for x in xrange(len(self.cache)):
            result += "{:^4X} ".format(x)
            result += str(self.cache[x])
            result += "\n"
        return result

    def get_slot(self, address):
        slot_id = (address >> 4) & 0xf
        return self.cache[slot_id]

    def read_address(self, address):
        slot = self.get_slot(address)
        return slot.read_slot(address)

    def write_address(self, address, datum):
        slot = self.get_slot(address)
        return slot.write_slot(address, datum)
