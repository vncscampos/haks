#!/usr/bin/python

import socket, sys

ip = raw_input("Digite o IP: ")

for port in range(1, 65535):
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if (mysocket.connect_ex((ip, port)) == 0):
		print "Porta", port, "[ABERTA]"
	mysocket.close()
