#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Benjamin Weeks
CS472 Project 2
November, 1st, 2015

Command Line Interface
"""

from main import Cache


class Cmd(object):
    def __init__(self):
        self.cache = Cache()


    def get_address(statement):
        address = raw_input("What address would you like {}\n?".format(statement))
        return address


    def get_action():
        action = raw_input("(R)ead, (W)rite, or (D)isplay Cache?\n")
        return action
        return


    def read_address(self, address):
        result = self.cache.read_address(address)
        print "At that byte there is the value {0:x} ({1})".format(result)
        return


    def write_data(self, address):
        datum = raw_input("What datum would you like to write at that address?\n")
        datum = int(datum, 16)
        self.cache.write_address(address, datum)
        print ("Value {:x} has been written to address {:x}.".format(datum, address))
        return


    def display_cache(self):
        print str(self.cache)
        return


    def run(self):
        while True:
            action = get_action()[0].lower()
            if action == "r":
                address = int(get_address("read"), 16)
                read_address(self, address)
            elif action == "w":
                address = int(get_address("to write to"), 16)
                write_data(self, address)
            elif action == "d":
                display_cache(self)
            else:
                break
        return
