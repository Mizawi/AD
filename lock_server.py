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
import pickle, struct
import time


###############################################################################

class resource_lock:
    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        self.id =
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
        
        self.N = N
        self.K = K
        self.Y = Y
        self.T = T

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        pass # Remover esta linha e fazer implementação da função

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
        pass # Remover esta linha e fazer implementação da função

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """
        pass # Remover esta linha e fazer implementação da função

    def test(self,resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso 
        esteja bloqueado ou inativo.
        """
        pass # Remover esta linha e fazer implementação da função

    def stat(self,resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado, dos 
        K bloqueios permitidos.
        """
        pass # Remover esta linha e fazer implementação da função

    def stat_y(self):
        """
        Retorna o número de recursos bloqueados num dado momento do Y permitidos.
        """
        pass # Remover esta linha e fazer implementação da função

    def stat_n(self):
        """
        Retorna o número de recursos disponíneis em N.
        """
        pass # Remover esta linha e fazer implementação da função
		
    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        output = ""
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
PORT = sys.argv[2]

i = 0
listener_socket = su.create_tcp_server_socket(HOST, PORT, queue_size)

global i
    
while True:

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