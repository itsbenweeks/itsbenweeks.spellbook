#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Benjamin Weeks
CS472 Project 2
November, 1st, 2015

Command Line Interface
"""

from cache import Cache


class Cmd(object):
    def __init__(self):
        self.cache = Cache()

    def get_address(self, statement):
        address = raw_input("What address would you like {}?\n".format(statement))
        return address

    def get_action(self):
        action = raw_input("(R)ead, (W)rite, or (D)isplay Cache?\n")
        if action is '':
            action = 'q'
        return action.lower()[0]

    def read_address(self, address):
        result = self.cache.read_address(address)
        print "At that byte there is the value {0:X} ({1})".format(result[0],
                                                                   result[1])
        return

    def write_data(self, address):
        datum = raw_input("What datum would you like to write at that address?\n")
        datum = int(datum, 16)
        result = self.cache.write_address(address, datum)
        print ("Value {:X} has been written to address {:X}. ({})".format(
            datum,
            address,
            result))
        return

    def display_cache(self):
        print str(self.cache)
        return

    def run(self):
        while True:
            action = self.get_action()
            if action == "r":
                address = int(self.get_address("read"), 16)
                self.read_address(address)
            elif action == "w":
                address = int(self.get_address("to write to"), 16)
                self.write_data(address)
            elif action == "d":
                self.display_cache()
            else:
                break
        return
