#!/bin/python3
# -*- coding: utf-8 -*-
# -*- coded by: Fzin -*-

import argparse
from sys import exit
from modules import sckt


EXE = False
MAX = 1

parser = argparse.ArgumentParser(usage="python3 netkit.py", description="Netkit is a Swiss army knife tool.")
parser.add_argument("-l", help="To listen a port.", metavar="<port>")
parser.add_argument("-m", help="To set max of connections.", metavar="<number>")
parser.add_argument("-c", help="To connect in something.", metavar="<address> <port>", nargs="*")
parser.add_argument("-e", help="To exec one command.", metavar="<command>")
parser.add_argument("--dnsr", help="To exec dns resolver.", metavar="<domain>")
parser.add_argument("--rdnsr", help="To exec reverse dns resolver.", metavar="<address>")
parser.add_argument("--sqli", help="To unlock sqli automation commands.", metavar="<url> [options]")

args = parser.parse_args()


if None == args.c and None == args.l and None == args.m and None == args.e and None == args.dnsr and None == args.rdnsr:
	print('Netkit: missing arguments. Type -h to see the list of commands.')

if args.m:
	MAX = int(args.m)
if args.e:
	EXE = args.e

if args.l:
	if not EXE == False:
		sckt.bind_tcp(host="0.0.0.0", port=int(args.l), execution=EXE, max=MAX)
	else:
		sckt.bind_tcp(host="0.0.0.0", port=int(args.l), max=MAX)

elif args.c:
	try:
		if not EXE == False:
			sckt.connect_tcp(host=args.c[0], port=int(args.c[1]), execution=EXE)
		else:
			sckt.connect_tcp(host=args.c[0], port=int(args.c[1]))

	except ConnectionRefusedError:
		print('Netkit: Connection Refused')
		sckt.error()
	except IndexError:
		print("Netkit: missing arguments.")
		sckt.error()
	except ValueError:
		print("Netkit: Invalid argument")
		sckt.error()
	except:
		print("Netkit: One error as occurred.")
		sckt.error()

elif args.dnsr:
	try:
		sckt.dns_resolver(domain=args.dnsr)
	except NameError:
		pass

elif args.rdnsr:
	try:
		sckt.dns_reverse_resolver(address=args.rdnsr)
	except NameError:
		pass
