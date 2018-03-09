# coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 01
Números de aluno: 48314 | 48292 | 48299
"""
# Zona para fazer imports
import sys
from net_client import server
from sys import argv

# Programa principal


print "ID Client: ", argv[3]

while True:

    cmd = raw_input("comando > ")

    if "LOCK" in cmd:

        if len(cmd.split()) == 3:

            client_socket = server(argv[1], argv[2])
            socket = client_socket.connect()
            resposta = client_socket.send_receive(socket, cmd)

            print resposta

            client_socket.close(socket)
            print "Ligação Terminada"

        else:

            print "Parametros Errados"

    elif "RELEASE" in cmd:
        if len(cmd.split()) == 3:

            client_socket = server(argv[1], argv[2])
            socket = client_socket.connect()
            resposta = client_socket.send_receive(socket, cmd)

            print resposta

            client_socket.close(socket)
            print "Ligação Terminada"

        else:
            print "Parametros Errados"

    elif "TEST" in cmd:
        if len(cmd.split()) == 2:

            client_socket = server(argv[1], argv[2])
            socket = client_socket.connect()
            resposta = client_socket.send_receive(socket, cmd)

            print resposta

            client_socket.close(socket)
            print "Ligação Fechada"

        else:
            print "Parametros Errados"

    elif "STATS" in cmd:

        if "STATS-Y" in cmd.split():

            if len(cmd.split()) == 1:
                client_socket = server(argv[1], argv[2])
                socket = client_socket.connect()
                resposta = client_socket.send_receive(socket, cmd)

                print resposta

                client_socket.close(socket)
                print "Ligação Terminada"

            else:
                print "Parametros Errados"

        elif "STATS-N" in cmd.split():

            if len(cmd.split()) == 1:

                client_socket = server(argv[1], argv[2])
                socket = client_socket.connect()
                resposta = client_socket.send_receive(socket, cmd)

                print resposta

                client_socket.close(socket)
                print "Ligação Terminada"

            else:
                print "Parametros Errados"
        else:

            if len(cmd.split()) == 2:

                client_socket = server(argv[1], argv[2])
                socket = client_socket.connect()
                resposta = client_socket.send_receive(socket, cmd)

                print resposta

                client_socket.close(socket)
                print "Ligação Terminada"

            else:
                print "Parametros Errados"
    elif 'EXIT' in cmd:

        sys.exit()

