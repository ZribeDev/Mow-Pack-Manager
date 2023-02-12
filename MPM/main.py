#!/usr/bin/env python

import sys
import os

def mpm_install(package):
    print(package)
    return
args = []

for arg in sys.argv:
    if (arg == sys.argv[0]):
        continue
    else:
        args.append(arg)
if len(args) == 0:
    print("Incorrect Arguments! use -h to get help!")
    sys.exit()
commands = ["-i","install", "-r","remove", "-h","help"]
if args[0] not in commands:
    print("Incorrect Arguments! use -h to get help!")
    sys.exit()

if args[0] == "install" or args[0] == "-i":
    
    if len(args) == 1:
        print("Incorrect Arguments! use -h to get help!")
        sys.exit()
    mpm_install(args[1])