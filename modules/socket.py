import socket
import threading
import os, subprocess

from sys import exit

class sckt:
	def __init__(self):
		self.tm = False
		self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def message_send(self):
		try:
			while self.tm:
				msg = input()
				msg = msg + '\n'
				msg = msg.encode('utf-8')
				self.sckt.send(msg)
		except BrokenPipeError:
			print('Netkit: Broken pipe')
			self.error()
		except:
			self.error()

	def message_recv(self):
		while self.tm:
			try:
				message = self.sckt.recv(2048).decode('utf-8')
				if len(message) >= 1:
					print(message[0:-1])
			except:
				self.error()

	def threads(self):
		try:
			thread = threading.Thread(target=self.message_send, args=())
			thread.start()
		except:
			self.error()

	def bind_tcp(self, host, port, execution=False, max=None):
		try:
			self.sckt.bind((host, port))
		except socket.error as Error:
			if str(Error) == '[Errno 13] Permission denied':
				print('Netkit: Permission Denied')
			elif str(Error) == '[Errno 98] Address already in use':
				print("Netkit: Address already in use")
			
			exit()
		except KeyboardInterrupt:
			exit()
		
		self.sckt.listen(max)
		print(f'Netkit: Listen {host}:{port}')
		
		if not 1 == max:
			print(f'Netkit: Maximum connections set is {max}')
		
		try:
			conn, addr = self.sckt.accept()
		except KeyboardInterrupt:
			exit()
		
		print(f'Netkit: Connection from {addr[0]}:{addr[1]}')
		self.tm = True
		
		if not execution == False:
			os.dup2(conn.fileno(), 0)
			os.dup2(conn.fileno(), 1)
			os.dup2(conn.fileno(), 2)
			
			if execution == '/bin/bash' or execution == 'bash':
				execution = '/bin/bash -i'
			
			subprocess.call(execution, shell=True)
		else:
			self.threads()
			self.message_recv()

	def connect_tcp(self, host, port, execution=False):
		try:
			self.sckt.settimeout(15)
			self.sckt.connect((host, port))
		except socket.timeout:
			print('Netkit: Timeout')
			self.sckt.close()

		self.tm = True
		print(f'Netkit: Connected to {socket.gethostbyname(host)}:{port}')

		if not execution == False:
			os.dup2(self.sckt.fileno(), 0)
			os.dup2(self.sckt.fileno(), 1)
			os.dup2(self.sckt.fileno(), 2)
			
			if execution == '/bin/bash' or execution == 'bash':
				execution = 'bash -i'

			subprocess.call(execution, shell=True)
		else:
			self.threads()
			self.message_recv()

	def dns_resolver(self, domain):
		try:
			print(socket.gethostbyname(domain))
		except socket.gaierror:
			print('Netkit: Domain invalid')

	def dns_reverse_resolver(self, address):
		try:
			print(socket.gethostbyaddr(address)[0])
		except socket.gaierror:
			print('Netkit: Address invalid')

	def error(self):
		try:
			self.sckt.close()
		except:
			self.sckt.close()

		self.tm = False
		exit()
