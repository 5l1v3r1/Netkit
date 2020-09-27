import socket
import threading
import os, subprocess

from sys import exit

class sckt:
	def __init__(self):
		self.tm = False

	def message_send(self):
		try:
			while self.tm:
				msg = input()
				msg = msg + '\n'
				msg = msg.encode('utf-8')
				self.conn.send(msg)
		except socket.error as ERROR:
			if str(ERROR) != "[Errno 9] Bad file descriptor":
				print(f"Netkit: {self.error_resolver(ERROR)}")
			self.error()

		except BrokenPipeError:
			print('Netkit: Broken pipe')
			self.error()

		except KeyboardInterrupt:
			self.error()

		except Exception as ERROR:
			print(f"Netkit: {self.error_resolver(ERROR)}")
			exit()

	def message_recv(self):
		while self.tm:
			try:
				message = self.conn.recv(2048).decode('utf-8')
				if len(message) >= 1:
					print(message[0:-1])

			except socket.error as ERROR:
				if str(ERROR) != "[Errno 9] Bad file descriptor":
					print(f"Netkit: {ERROR}")
				self.error()

			except BrokenPipeError:
				print("Netkit: Broken pipe")
				self.error()

			except KeyboardInterrupt:
				self.error()

			except Exception as ERROR:
				print(f"Netkit: {self.error_resolver(ERROR)}")
				exit()
	def threads(self):
		try:
			thread = threading.Thread(target=self.message_send, args=())
			thread.start()
		except:
			self.error()

	def bind_tcp(self, host, port, execution=False, max=1):
		try:
			self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sckt.bind((host, port))
		except socket.error as ERROR:
			print(f"Netkit: {self.error_resolver(ERROR)}")
			exit()

		except KeyboardInterrupt:
			exit()

		self.sckt.listen(max)
		print(f'Netkit: Listen {host}:{port}')

		if not 1 == max:
			print(f'Netkit: Maximum connections set is {max}')

		try:
			self.conn, self.addr = self.sckt.accept()
		except KeyboardInterrupt:
			exit()

		print(f'Netkit: Connection from {self.addr[0]}:{self.addr[1]}')
		self.tm = True

		if not execution == False:
			os.dup2(self.conn.fileno(), 0)
			os.dup2(self.conn.fileno(), 1)
			os.dup2(self.conn.fileno(), 2)

			if execution == '/bin/bash' or execution == 'bash':
				execution = '/bin/bash -i'

			subprocess.call(execution, shell=True)
		else:
			self.threads()
			self.message_recv()

	def connect_tcp(self, host, port, execution=False):
		try:
			self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.conn.connect((host, port))
		except Exception as ERROR:
			print(f'Netkit: {self.error_resolver(ERROR)}')
			self.error()

		self.tm = True
		print(f'Netkit: Connected to {socket.gethostbyname(host)}:{port}')

		if not execution == False:
			os.dup2(self.conn.fileno(), 0)
			os.dup2(self.conn.fileno(), 1)
			os.dup2(self.conn.fileno(), 2)

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
			self.conn.close()

		self.tm = False
		exit()

	def error_resolver(self, error):
		error = str(error)
		if "]" in error:
			error = error[error.find("]")+2:]
		return error
