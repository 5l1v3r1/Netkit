#!/bin/python3
# -*- coding: utf-8 -*-
#coded by: Fzin

from sys import argv
from modules.modules import error
import sys
from subprocess import call, check_output as out

del argv[0]

icon = ("""

███╗   ██╗███████╗████████╗██╗  ██╗██╗████████╗
████╗  ██║██╔════╝╚══██╔══╝██║ ██╔╝██║╚══██╔══╝
██╔██╗ ██║█████╗     ██║   █████╔╝ ██║   ██║
██║╚██╗██║██╔══╝     ██║   ██╔═██╗ ██║   ██║
██║ ╚████║███████╗   ██║   ██║  ██╗██║   ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝

""")

try:
    out("which lolcat", shell=True)
except:
    call("pip3 install lolcat", shell=True)

try: call(f"echo '''{icon}''' | lolcat", shell=True)
except KeyboardInterrupt: sys.exit()

if '-h' in argv:
	if argv[0] == '-h':
		print(
'''
Netkit Help:

-l <port>\t\t\tTo listen a port.
-m <number>\t\t\tTo set max of connections.
-c <address> <port>\t\tTo connect in something.
-e <command>\t\t\tTo exec one command.
--dnsr <domain>\t\t\tTo exec dns resolver.
--rdnsr <address>\t\tTo exec reverse dns resolver.
''')
		sys.exit()


elif argv == []: print('Netkit: missing arguments. Type -h to see the list of commands.')

args = {}

max = 1
if '-m' in argv:
	try:
		max = int(argv[(argv.index('-m')+1)])
	except KeyError and IndexError:
		print('Netkit: missing arguments')
		sys.exit()

exe = False
if '-e' in argv:
		try:
			exe = argv[(argv.index('-e')+1)]
		except KeyError and IndexError:
			print('Netkit: missing arguments')
			sys.exit()

for i in argv:
	if i == '-l' and args == {}:
		try:
			args['listen'] = int(argv[(argv.index('-l')+1)])
		except KeyError and IndexError:
			print('Netkit: missing arguments')
			sys.exit()
		except ValueError:
			print("Netkit: invalid argument.")
			sys.exit()

		from modules.modules import bind_tcp
		if exe != False:
			bind_tcp("0.0.0.0", args['listen'], exe, max=max)
		else:
			bind_tcp("0.0.0.0", args['listen'], max=max)

	elif i == '-c' and args == {}:
		try:
			args['host_c'] = argv[(argv.index('-c')+1)]
			args['port_c'] = int(argv[(argv.index(args['host_c'])+1)])
		except KeyError and IndexError:
			print('Netkit: missing arguments')
			sys.exit()
		except ValueError:
			print("Netkit: invalid argument.")
			sys.exit()
		from modules.modules import connect_tcp
		try:
			if exe != False:
				connect_tcp(args['host_c'], args['port_c'], exe)
			else:
				connect_tcp(args['host_c'], args['port_c'])
		except ConnectionRefusedError:
			print('Netkit: Connection Refused')
			pass
		except:
			error()

	elif i == '--dnsr':
		try:
			domain = argv[(argv.index('--dnsr')+1)]
		except IndexError:
			print('Netkit: missing arguments')
			sys.exit()
		from modules.modules import dns_resolver
		try:
			dns_resolver(domain)
		except NameError:
			pass
	elif i == '--rdnsr':
		try:
			host = argv[(argv.index('--rdnsr')+1)]
		except IndexError:
			print('Netkit: missing arguments')
			sys.exit()
		from modules.modules import dns_reverse_resolver
		try:
			dns_reverse_resolver(host)
		except NameError:
			pass
