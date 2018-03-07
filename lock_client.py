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

# Programa principal
HOST = sys.argv[1]
PORT = sys.argv[2]
a = True

while a:
    client_socket = su.create_tcp_client_socket(HOST, PORT)

    msg = list(raw_input("Escreva uma mensagem para enviar --> "))
    
    if 'EXIT' in msg:

        client_socket.sendall('EXIT')
        print "Client closed"
        a = False
        
    else:
        msg_bytes = pickle.dumps(msg, -1)
        size_bytes = struct.pack('!i', len(msg_bytes))
        client_socket.sendall(msg_bytes)
        client_socket.sendall(size_bytes)
        dados_recebidos = su.receive_all(client_socket, 1024)
        print 'Recebi %s' % dados_recebidos

    client_socket.close()


