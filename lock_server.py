#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
"""

# Zona para fazer importação

import time
import sock_utils
from sys import argv
from multiprocessing import Semaphore

###############################################################################
s = Semaphore(1)
###############################################################################

class resource_lock:
    def __init__(self, K):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        self.block = False
        self.nBlock = 0
        self.BlockClients = []
        self.time_limit = 0
        self.time = 0
        self.maxclients = K

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
        if len(self.BlockClients) < self.maxclients:

            self.block = True
            self.nBlock += 1
            if client_id not in self.BlockClients:
                self.BlockClients.append(client_id)
            self.time = time.time()
            self.time_limit = time_limit

            return True

        else:

            return False

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.block = False
        self.BlockClients = []
        self.time_limit = 0

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        if client_id in self.BlockClients:
            if len(self.BlockClients) > 1:
                self.BlockClients.remove(client_id)
            elif len(self.BlockClients) == 1:
                self.block = False
                self.BlockClients = []
            return True

        else:

            return False

    def test(self):
        """
        Retorna o estado de bloqueio do recurso.
        """
        return self.block

    def stat(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado.
        """
        return self.nBlock

    def stat_k(self):
        """
        Retorna o número de bloqueios em simultâneo em K.
        """
        return len(self.BlockClients)


###############################################################################

class lock_pool:
    def __init__(self, N, K):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        Define também K, o valor máximo do número de bloqueios simultâneos a um recurso qualquer.
        """

        self.ArrayLock = []

        for i in range(N):
            self.ArrayLock.append([i, resource_lock(K)])
        self.K = K

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        for resource in self.ArrayLock:

            if time.time() - resource[1].time > resource[1].time_limit:
                resource[1].urelease()

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit.
        O bloqueio do recurso só é possível se K ainda não foi excedido para este
        recurso. É aconselhável implementar um método _try_lock para vericar estas condições. 
        Retorna True em caso de sucesso e False caso contrário.
        """
        start_time = time.time()
        while (start_time - time.time()) < time_limit:
            s.acquire()
            for resource in self.ArrayLock:
                if resource_id == resource[0]:
                    if resource[1].stat_k() < self.K:
                        s.release()
                        return resource[1].lock(int(client_id), time_limit)

            s.release()
        return False

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """
        for resource in self.ArrayLock:
            if resource[0] == resource_id:
                return resource[1].release(int(client_id))

    def test(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso
        contrário.
        """
        for resource in self.ArrayLock:
            if resource[0] == resource_id:
                return resource[1].test()

    def stat(self, resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado.
        """
        for resource in self.ArrayLock:
            if resource[0] == resource_id:
                return resource[1].stat()

    def stat_k(self, resource_id):
        """
        Retorna o número de bloqueios simultâneos no recurso resource_id.
        """
        for resource in self.ArrayLock:
            if resource[0] == resource_id:
                return resource[1].stat_k()

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
                output += "Recurso ID: " + str(resource[0]) + " bloqueado pelo(s) o cliente(s):" + clients + " até aos " + str(resource[1].time_limit) + " Segundos, Tempo passado: " + str(time.time() - resource[1].time) + " Segundos\n"

            else:
                if resource[0] == 0:
                    output += "\nRecurso ID: " + str(resource[0]) + " desbloqueado  \n"
                else:
                    output += "Recurso ID: " + str(resource[0]) + " desbloqueado  \n"



        # Acrescentar na output uma linha por cada recurso bloqueado, da forma:
        # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
        # <instante limite da concessão do bloqueio>
        #
        # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
        # recurso <número do recurso> desbloqueado

        return output


###############################################################################

# código do programa principal


sock = sock_utils.create_tcp_server_socket('', int(argv[1]), 10)

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

    data = sock_utils.receive_all(conn_sock, 1024)
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
    # Comando Stats_k
    elif "Stats_k" in msg:
        conn_sock.sendall(str(lock_pool.stat_k((int(msg[1])))))

    else:
        conn_sock.sendall("UNKNOWN COMMAND")
        conn_sock.close()

sock.close()
