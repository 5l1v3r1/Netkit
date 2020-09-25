#!/bin/python3
# -*- coding: utf-8 -*-
# -*- coded by: Fzin -*-

from sys import argv

sckt = None
if "--sqli" in argv:
	from modules.sqli import sqli
	sqli = sqli()
	exit()

else:
	from modules.socket import sckt
	sckt = sckt()
