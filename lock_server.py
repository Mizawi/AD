#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo:
Números de aluno:
"""

# Zona para fazer importação

import socket as s
import sock_utils as su
import sys, os
from sys import argv
import pickle, struct
import time


###############################################################################

class resource_lock:
    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.
        """

        self.block = False
        self.nBlock = 0
        self.client = "NONE"
        self.time_limit = 0
        self.time = 0

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """

        if self.block != True or self.block != "Unavailable":
            self.block = True
            self.client = client_id
            self.time = time.time()
            self.time_limit = time_limit

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.block = False
        self.client = "NONE"
        self.time = 0
        self.time_limit = 0

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        if self.client == client_id:
            self.block = False
            self.client = "NONE"
            self.time = 0
            self.time_limit = 0

    def test(self):
        """
        Retorna o estado de bloqueio do recurso ou inativo, caso o recurso se
        encontre inativo.
        """
        return self.block

    def stat(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado em k.
        """
        return self.nBlock

    def disable(self):
        """
        Coloca o recurso inativo/indisponível incondicionalmente, alterando os
        valores associados à sua disponibilidade.
        """
        self.block = "Unavailable"
        self.client = "NONE"
        self.time = 0


###############################################################################

class lock_pool:
    def __init__(self, N, K, Y, T):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        Define K, o número máximo de bloqueios permitidos para cada recurso. Ao
        atingir K, o recurso fica indisponível/inativo.
        Define Y, o número máximo permitido de recursos bloqueados num dado
        momento. Ao atingir Y, não é possível realizar mais bloqueios até que um
        recurso seja libertado.
		Define T, o tempo máximo de concessão de bloqueio.
        """
        lock_array = []

        for i in range(N):
            lock_array.append([i, resource_lock()])
        self.K = K
        self.Y = Y
        self.T = T
        self.locks = 0

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        for resource in self.lock_array:
            if resource[1].time >= self.T:
                resource[1].urelease()

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit.
        O bloqueio do recurso só é possível se o recurso estiver ativo, não
        bloqueado ou bloqueado para o próprio requerente, e Y ainda não foi
        excedido. É aconselhável implementar um método __try_lock__ para
        verificar estas condições.
        Retorna True em caso de sucesso e False caso contrário.
        """
        for resource in self.lock_array:

            if resource[1].test() == True:
                return False
            else:
                if resource_id.nBlock <= self.Y:
                    resource_id.lock(client_id, time_limit)
                    self.locks += 1
                    return True

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """

        for resource in self.lock_array:
            if resource[0] == resource_id:
                return resource[1].release(client_id)

    def test(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado False caso
        esteja desbloqueado ou inativo.
        """
        for resource in self.lock_array:
            if resource[0] == resource_id:
                if resource[1].test() == "Unavailable":
                    return False
                else:
                    return resource[1].test()

    def stat(self, resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado, dos
        K bloqueios permitidos.
        """
        for resource in self.lock_array:
            if resource[0] == resource_id:
                return resource[1].stat()

    def stat_y(self):
        """
        Retorna o número de recursos bloqueados num dado momento do Y permitidos.
        """
        return self.locks

    def stat_n(self):
        """
        Retorna o número de recursos disponíveis em N.
        """
        n_available = 0

        for resource in self.lock_array:
            if resource[1].test() == False:
                n_available += 1

        return n_available

    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        output = ""

        for resource in self.ArrayLock:
            if resource[1].test():
                clients = " "
                for client in resource[1].BlockClients:
                    clients += "" + str(client) + ","
                print resource[1].time
                output += ("Recurso ID: " + str(
                    resource[0]) + " bloqueado pelo(s) o cliente(s):" + clients + " até aos " + str(
                    resource[1].time_limit) + " Segundos, Tempo passado: " + str(
                    time.time() - resource[1].time) + " Segundos\n")

            else:
                if resource[0] == 0:
                    output += "\nRecurso ID: " + str(resource[0]) + " desbloqueado  \n"
                else:
                    output += "Recurso ID: " + str(resource[0]) + " desbloqueado  \n"

        #
        # Acrescentar na output uma linha por cada recurso bloqueado, da forma:
        # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
        # <instante limite da concessão do bloqueio>
        #
        # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
        # recurso <número do recurso> desbloqueado
        # Caso o recurso não esteja inativo a linha é simplesmente da forma:
        # recurso <número do recurso> inativo
        #
        return output


###############################################################################

# código do programa principal


HOST = '127.0.0.1'
PORT = argv[2]


i = 0
listener_socket = su.create_tcp_server_socket(HOST, PORT)

global i

while True:

    sock = su.create_tcp_server_socket('', int(argv[1]), 10)

    print "Nº Resources: ", argv[2]
    print "Nº Maximo de Utilizadores num Recurso: ", argv[3]
    print "Tempo Limite:", argv[4], "\n"

    lock_pool = lock_pool(int(argv[2]), int(argv[3]))

    start_time = time.time()

    while True:

        print "Now Listening...\n"

        print lock_pool.__repr__

        (conn_sock, addr) = sock.accept()

        print "Connected to: ", addr, "\n"

        data = su.receive_all(conn_sock, 1024)
        msg = data.split()

        lock_pool.clear_expired_locks()

        # Verifica se esse recurso existe
        if int(msg[1]) > (int(argv[2]) - 1):
            conn_sock.sendall("UNKNOWN RESOURCE")
        # Commando Lock
        elif "Lock" in msg:
            Estado = lock_pool.lock(int(msg[1]), int(msg[2]), int(argv[4]))
            if Estado == True:
                print "Resource: ", msg[1], "Locked"
                conn_sock.sendall("OK")
                conn_sock.close()
            else:
                conn_sock.sendall("NOK")
                conn_sock.close()
        # Comando Release
        elif "Release" in msg:
            Estado = lock_pool.release(int(msg[1]), int(msg[2]))
            if Estado == True:
                print "Resource: ", msg[1], "Released"
                conn_sock.sendall("OK")
                conn_sock.close()
            else:
                conn_sock.sendall("NOK")
                conn_sock.close()
        # Comando Test
        elif "Test" in msg:
            Estado = lock_pool.test(int(msg[1]))
            if Estado == True:
                conn_sock.sendall("LOCKED")
            else:
                conn_sock.sendall("NOT LOCKED")
        # Comando Stats
        elif "Stats" in msg:
            conn_sock.sendall(str(lock_pool.stat(int(msg[1]))))
        # Comando Stats_y
        elif "Stats y" in msg:
            conn_sock.sendall(str(lock_pool.stat_y()))
        # Comando Stats_n
        elif "Stats n" in msg:
            conn_sock.sendall(str(lock_pool.stat_n()))

        else:
            conn_sock.sendall("UNKNOWN COMMAND")
            conn_sock.close()

listener_socket.close()