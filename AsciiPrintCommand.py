#!/usr/bin/python
# coding=utf-8

# This script provides a command to pretty-print a string with mixed ASCII and
# non-ASCII characters, as requested in this question
# https://stackoverflow.com/q/16031100/391161
# REQUIRES: At least GNU gdb (GDB) 7.7

from __future__ import print_function
import re
import sys
import gdb
import string

class PrettyPrintString(gdb.Command):

  "Command to print strings with a mix of ascii and hex."

  def __init__(self):
    super(PrettyPrintString, self).__init__("ascii-hex-print",
        gdb.COMMAND_DATA,
        gdb.COMPLETE_EXPRESSION, True)
    gdb.execute("alias -a xp = ascii-hex-print", True)

  def invoke(self, arg, from_tty):
    arg = arg.strip()
    if arg == "":
      print("Argument required (starting display address).")
      return
    max_print_len = sys.maxint
    if arg.startswith("*"):
      lengths = re.findall("@(\d+)$", arg)
      if len(lengths) == 1:
        max_print_len = int(lengths[0])
    startingAddress = gdb.parse_and_eval(arg)
    p = 0
    print('"', end='')
    if max_print_len == sys.maxint:
      while startingAddress[p] != ord("\0"):
        charCode = int(startingAddress[p].cast(gdb.lookup_type("unsigned char")))
        if chr(charCode) in string.printable:
          print("%c" % chr(charCode), end='')
        else:
          print("\\x%x" % charCode, end='')
        p += 1
    else:
      while p < max_print_len:
        charCode = int(startingAddress[p].cast(gdb.lookup_type("unsigned char")))
        if chr(charCode) in string.printable:
          print("%c" % chr(charCode), end='')
        else:
          print("\\x%x" % charCode, end='')
        p += 1
    print('"')

  def __del__(self):
    pass

PrettyPrintString()
