#!/usr/bin/env python

import sys
import os
import requests

servers = {
    "github": "https://raw.githubusercontent.com/ZribeDev/Mow-Pack-Manager/master/mpm_repositories/"
}
rep_server = servers["github"]


def mpm_install(package):
    raw = requests.get(rep_server + package + ".rep")
    rawtext = raw.text
    if rep_server == servers["github"]:
        if (rawtext == "404: Not Found"):
            data = {
                "code":404,
                "message":rawtext
            }
            return data
    data = {
        "code":200,
        "message":rawtext
    }
    return data
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
    print(mpm_install(args[1])["code"])