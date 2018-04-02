# coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: 01
Números de aluno: 48299 | 48314 | 48292
"""

# Zona para fazer importação
import sock_utils
import socket
import sys
from sys import argv
import select as sel
from multiprocessing import Semaphore
import cPickle as p
import lock_skel as skel
from pprint import PrettyPrinter

###############################################################################
s = Semaphore(1)
pp = PrettyPrinter()
###############################################################################

#Tratamento do erro caso o endereço requisitado já esteja a ser usado
try:
    ListenSocket = sock_utils.create_tcp_server_socket('', int(argv[1]), 10)
except socket.error as s:
    print "O endereço já está a ser usado, modifique o valor do PORT"
    sys.exit()

print "Port: ", argv[1]
print "Nº Resources: ", argv[2]
print "Nº máximo de bloqueios permitidos para cada recurso: ", argv[3]
print "Nº máximo permitido de recursos bloqueados num dado: ", argv[4]
print "Tempo Limite:", argv[5], "\n"


lock_pool = skel.LockSkel(int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]))

SocketList = [ListenSocket]

while True:
    try:
        R, W, X = sel.select(SocketList, [], [])
        for sckt in R:
            if sckt is ListenSocket:
                (conn_sock, addr) = ListenSocket.accept()
                addr, port = conn_sock.getpeername()
                print 'Novo client ligado desde %s:%d' % (addr, port)
                SocketList.append(conn_sock)
            else:

                obj = p.loads(sock_utils.receive_all(conn_sock, 1024))

                if obj:
                    if obj[0] == 01:
                        sckt.close()
                        SocketList.remove(sckt)
                        print'Cliente fechou ligação'
                    else:
                        conn_sock.sendall(lock_pool.msgreceiver(obj, argv))
                        print "Objecto: ", pp.pprint(obj)
                else:
                    sckt.close()
                    SocketList.remove(sckt)
                    print'Cliente fechou ligação'

            lock_pool.lp.clear_expired_locks()

            print lock_pool.lp.__repr__()

    except EOFError:
        print "A ligação com o cliente foi encerrada"
        print " Á espera de nova ligação..."

