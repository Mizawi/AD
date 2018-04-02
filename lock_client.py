# coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 01
Números de aluno: 48314 | 48292 | 48299
"""

# Zona para fazer imports
import socket
from sys import argv
import lock_stub as ls
import pickle as p
from pprint import PrettyPrinter

# Programa principal


pp = PrettyPrinter()
comandos = {"LOCK", "RELEASE", "TEST", "STATS", "STATS-N", "STATS-Y"}


ID = argv[3]

print "ID :", argv[3]

connection = True

print 'Ligado pelo endereço local %s:%d' % (argv[1], int(argv[2]))


while connection:

    cmd = raw_input("comando > ")
    cmd = cmd.split(" ")

    # Tratamento do erro em caso que o servidor não esteja disponivel
    connected = False
    while connected == False:
        try:
            client_socket = ls.LockStub(argv[1], argv[2])
            connected = True
        except socket.error as s:
            print" Ocorreu um erro na ligação ao servidor"
            print"\n Aguarde enquanto o servidor se liga"

    if cmd[0] == "Q" or cmd[0] == "Quit":
        connection = False
        client_socket.close()

    elif cmd[0] not in comandos:
        print "Comando desconhecido, por favor introduza de novo"


    else:
        if "LOCK" == cmd[0]:
            if len(cmd) == 2:
                obj = p.loads(client_socket.lock([cmd[1], ID]))
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj)

                if obj[1] == 'True':
                    print "Recurso", cmd[1], "foi bloqueado"
                else:
                    print "Recurso", cmd[1], "não foi ou já está bloqueado"


            else:

                print "Parametros Errados"

        if "RELEASE" == cmd[0]:
            if len(cmd) == 2:
                obj = p.loads(client_socket.release([cmd[1], ID]))
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj)

                if obj[1] == 'True':
                    print "Recurso", cmd[1], "foi desbloqueado"
                else:
                    print "Recurso", cmd[1], "não foi ou já está desbloqueado"

            else:
                print "Parametros Errados"

        if "TEST" == cmd[0]:
            if len(cmd) == 2:
                obj = p.loads(client_socket.test([cmd[1]]))
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj)

                if obj[1] == 'True':
                    print "Recurso", cmd[1], "está bloqueado"
                elif obj[1] == 'Disable':
                    print "Recurso", cmd[1], "está desactivado"
                else:
                    print "Recurso", cmd[1], "não bloqueado"


            else:

                print "Parametros Errados"

        if "STATS-Y" == cmd[0]:
            print "Entrei aqui Y"
            if len(cmd) == 1:
                obj = p.loads(client_socket.stats_y())
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj)
                print obj[1], " recursos estão bloqueados em Y"

            else:

                print "Parametros Errados"

        if "STATS-N" == cmd[0]:
            if len(cmd) == 1:
                obj = p.loads(client_socket.stats_n())
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj)
                print obj[1], " recursos estão disponiveis"

            else:

                print "Parametros Errados"

        if "STATS" == cmd[0]:

            if len(cmd) == 2:
                obj = p.loads(client_socket.stats([cmd[1], ID]))
                client_socket.close()

                print "Objecto recebido:", pp.pprint(obj), "\n"
                print "O nº de bloqueios no recurso ", cmd[1], "em K foram ", obj[1]

            else:

                print "Parametros Errados"

