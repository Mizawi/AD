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



ListenSocket = sock_utils.create_tcp_server_socket('', int(argv[1]), 10)

print "Port: ", argv[1]
print "Nº Resources: ", argv[2]
print "Nº máximo de bloqueios permitidos para cada recurso: ", argv[3]
print "Nº máximo permitido de recursos bloqueados num dado: ", argv[4]
print "Tempo Limite:", argv[5], "\n"

lock_pool = skel.LockSkel(int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]))

SocketList = [ListenSocket]



while True:

    print "Now Listening...\n"

    (conn_sock, addr) = server_sock.accept()



    print "Connected to: ", addr, "\n"

    data = su.receive_all(conn_sock, 1024)

    msg = data.split()

    print msg

    lock_pool.clear_expired_locks()

    # Commando Lock
    if "LOCK" in msg:
        if int(msg[1]) > (int(argv[2]) - 1):
            conn_sock.sendall("UNKNOWN RESOURCE")
        else:
            if lock_pool.lock(int(msg[1]), int(msg[2]), int(argv[5])) == True:
                print "Resource ID: ", msg[1], "Locked"
                conn_sock.sendall("OK")
                conn_sock.close()
            elif lock_pool.lock(int(msg[1]), int(msg[2]), int(argv[5])) == "Unavailable":
                print "Resource ID: ", msg[1], "Unavailable"
                conn_sock.sendall("NOT AVAILABLE")
                conn_sock.close()
            elif lock_pool.lock(int(msg[1]), int(msg[2]), int(argv[5])) == False:
                conn_sock.sendall("NOK")
                conn_sock.close()
    # Comando Release
    elif "RELEASE" in msg:
        if int(msg[1]) > (int(argv[2]) - 1):
            conn_sock.sendall("UNKNOWN RESOURCE")
        else:
            if lock_pool.release(int(msg[1]), int(msg[2])):
                print "Resource: ", msg[1], "Released"
                conn_sock.sendall("OK")
                conn_sock.close()
            else:
                conn_sock.sendall("NOK")
                conn_sock.close()
    # Comando Test
    elif "TEST" in msg:
        if int(msg[1]) > (int(argv[2]) - 1):
            conn_sock.sendall("UNKNOWN RESOURCE")
        else:
            Estado = lock_pool.test(int(msg[1]))
            if Estado == True:
                conn_sock.sendall("LOCKED")
            elif Estado == "Unavailable":
                conn_sock.sendall("NOT AVAILABLE")
            elif Estado == False:
                conn_sock.sendall("NOT LOCKED")
    # Comando Stats
    elif "STATS" == msg[0]:
        if int(msg[1]) > (int(argv[2]) - 1):
            conn_sock.sendall("UNKNOWN RESOURCE")
        else:
            conn_sock.sendall(str(lock_pool.stat(int(msg[1]))))
    # Comando Stats_y
    elif "STATS-Y" == msg[0]:
        conn_sock.sendall(str(lock_pool.stat_y()))
    # Comando Stats_n
    elif "STATS-N" == msg[0]:
        conn_sock.sendall(str(lock_pool.stat_n()))

    else:
        conn_sock.sendall("UNKNOWN COMMAND")
        conn_sock.close()

    print lock_pool.__repr__()

sock.close()
