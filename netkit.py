#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by: Fzin

from argparse import ArgumentParser
from sys import exit
from modules import sckt

parser = ArgumentParser(usage='python3 netkit.py', description='Netkit is a Swiss Army Knife tool')

parser.add_argument('-l', help='Listen a port', metavar='<port>', type=int)
parser.add_argument('-m', help='Set max of connections', metavar='<number>', type=int)
parser.add_argument('-c', help='Connect to a server', metavar='<address> <port>', nargs="*")
parser.add_argument('-e', help='Execute a command', metavar='<command>')
parser.add_argument('--dnsr', help='Resolve a DNS', metavar='<domain>')
parser.add_argument('--rdns', help='Resolve a reverse DNS', metavar='<address>')
parser.add_argument("--sqli", help="To unlock sqli automation commands.", metavar="<url> [options]", nargs="*")

args = parser.parse_args()

if not any(list(vars(args).values())):
	print('Netkit: missing arguments. Use -h to display commands')

CMD = args.e if args.e else False
MAX = args.m if args.m else 1

try:
	if args.l:
		sckt.bind_tcp(host='0.0.0.0', port=args.l, execution=CMD, max=MAX)

	elif args.c:
		sckt.connect_tcp(host=args.c[0], port=int(args.c[1]), execution=CMD)

	elif args.dnsr:
		sckt.dns_resolver(domain=args.dnsr)

	elif args.rdns:
		sckt.dns_reverse_resolver(address=args.rdns)

except ConnectionRefusedError:
	print('Netkit: Connection refused')
	sckt.error()

except IndexError:
	print("Netkit: Missing arguments.")
	exit()

except ValueError:
	print("Netkit: Invalid arguments.")
	exit()

except Exception as ERROR:
	print(sckt.error_resolver(ERROR))
	exit()
