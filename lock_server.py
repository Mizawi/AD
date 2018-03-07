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


###############################################################################

class resource_lock:
    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        pass # Remover esta linha e fazer implementação da função

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
        pass # Remover esta linha e fazer implementação da função

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        pass # Remover esta linha e fazer implementação da função

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        pass # Remover esta linha e fazer implementação da função

    def test(self):
        """
        Retorna o estado de bloqueio do recurso ou inativo, caso o recurso se 
        encontre inativo.
        """
        pass # Remover esta linha e fazer implementação da função
    
    def stat(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado em k.
        """
        pass # Remover esta linha e fazer implementação da função

    def disable(self):
        """
        Coloca o recurso inativo/indisponível incondicionalmente, alterando os 
        valores associados à sua disponibilidade.
        """
        pass # Remover esta linha e fazer implementação da função

        
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
        if resource_id.test() == True:
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

    def test(self,resource_id):
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

    def stat(self,resource_id):
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



    a = True
    global i
    
    while a:

        conn_sock, addr = listener_socket.accept()

        print 'New Connection --> ', addr
       
        size_bytes = su.receive_all(conn_sock, 4)
        size = struct.unpack('!i', size_bytes)[0]

        msg_bytes = su.recieve_all(conn_sock, size)
        dados_recebidos = pickle.loads(msg_bytes)

        if 'get' in dados_recebidos:
            
            try:
                values = list(msg_dic.values())
                out = values[int(dados_recebidos[1])]
                conn_sock.send(str(out))
                print "GET command executed"

            except(ValueError):
                pass 

        elif 'list' in dados_recebidos:
            
            try:
                out = ""
                for value in msg_dic.values():
                    string = value[0]
                    out += string + ", "
            
                conn_sock.send(out)
                print "LIST command executed"

            except(ValueError):
                pass

        elif 'exit' in  dados_recebidos:
            
            print "EXIT command executed"
            print "Client disconnected"
        
       
        
        else:
            
            conn_sock.send("Invalid operation, please use 'GET', 'LIST', 'ADD' or 'REMOVE'.")    
            

    listener_socket.close()