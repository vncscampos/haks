#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

ip = raw_input("Digite o IP: ")

print "Porta   Serviço"
for port in range(1, 65535):
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if(mysocket.connect_ex((ip, port)) == 0):
		banner = mysocket.recv(1024)
		print port, "    ", banner
		mysocket.close()
