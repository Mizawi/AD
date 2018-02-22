#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
"""
# Zona para fazer imports

from net_client import server
from sys import argv

# Programa principal

client_socket = server(argv[1], argv[2])

ID = argv[3]

socket = client_socket.connect()

print "Connected to: ", argv[1]
print "ID Client: ", argv[3]

cmd = raw_input("comando > ")
cmd += " " + ID
	
resposta = client_socket.send_receive(socket, cmd)

print "Resposta: ", resposta

client_socket.close(socket)