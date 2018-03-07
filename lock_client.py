#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo:
Números de aluno: 
"""
# Zona para fazer imports
import socket as s
import sys
import sock_utils as su
import pickle, struct
from net_client import server
from sys import argv

# Programa principal

HOST = sys.argv[1]
PORT = sys.argv[2]

client_socket = server(argv[1], argv[2])
socket = client_socket.connect()

print "Connected to: ", argv[1]
print "ID Client: ", argv[3]

while True:


    cmd = raw_input("comando > ")
    cmd += " " + argv[3]

    if 'EXIT' in msg:

        print "Client connection closed"
        client_socket.close()
        sys.exit()

    else:

        cmd = raw_input("comando > ")
        cmd += " " + ID

        resposta = client_socket.send_receive(socket, cmd)

        print "Resposta: ", resposta





