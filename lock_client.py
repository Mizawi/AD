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
import lock_stub as ls
import pickle as p
from pprint import PrettyPrinter

# Programa principal


pp = PrettyPrinter()


ID = argv[3]


print "Connected to: ", argv[1]
print "ID Client: ", argv[3]
client_socket = ls.LockStub(argv[1], argv[2])

connection = True

while connection:

    cmd = raw_input("comando > ").split("")
    print "\n"

    if cmd[0] == "Q" or cmd[0] == "Quit":
        connection = False
        print "Conexão encerrada"
        client_socket.close()

    else:

        if "LOCK" == cmd[0]:
            if len(cmd) == 3:
                obj = p.loads(client_socket.lock([cmd[1], ID]))
            else:
                print "Parametros Errados"

        if "RELEASE" == cmd[0]:
            if len(cmd) == 3:
                obj = p.loads(client_socket.release([cmd[1], ID]))
            else:
                print "Parametros Errados"

        if "TEST" == cmd[0]:
            if len(cmd) == 2:
                obj = p.loads(client_socket.lock([cmd[1], ID]))
            else:
                print "Parametros Errados"

        if "STATS-Y" == cmd[0]:
            if len(cmd) == 1:
                obj = p.loads(client_socket.stats_y())
            else:
                print "Parametros Errados"

        if "STATS-N" == cmd[0]:
            if len(cmd) == 1:
                obj = p.loads(client_socket.stats_n())
            else:
                print "Parametros Errados"
        if "STATS" == cmd[0]:
            if len(cmd) == 2:
                obj = p.loads(client_socket.stats([cmd[1], ID]))
            else:
                print "Parametros Errados"

        print "O Objecto é:"
        pp.pprint(obj)

        print "Resposta: ", obj[1]
        print "\n"

        client_socket = ls.LockStub(argv[1], argv[2])
        print "Connected to: ", argv[1]
        print "ID Client: ", argv[3]


