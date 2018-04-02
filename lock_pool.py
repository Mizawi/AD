# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicações distribuídas - Projeto 1 - lock_pool.py
Grupo: 01
Números de aluno: 48314 | 48299 | 48292
"""

import sock_utils as su
from sys import argv
import time


###############################################################################

class resource_lock:
    def __init__(self, K):
        """
        Define e inicializa as características de um LOCK num recurso.
        """

        self.block = False
        self.nBlock = 0
        self.client = "NONE"
        self.time_limit = 0
        self.time = 0
        self.K = K

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """

        if self.block == False:
            if self.nBlock < self.K:
                    self.block = True
                    self.client = client_id
                    self.time = time.time()
                    self.time_limit = time_limit
                    self.nBlock += 1
                    return True
            else:
                return "Unavailable"
        else:
            return False

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
            return True
        return False

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

        self.lock_array = []

        for i in range(1, N+1):
            self.lock_array.append([i, resource_lock(K)])
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
            if time.time() - resource[1].time >= self.T:
                if resource[1].test() == True:
                    self.locks -= 1
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
        for re in self.lock_array:
            if re[1].client == client_id:
                if re[0] != resource_id:
                    return False

        for resource in self.lock_array:

            if resource[0] == resource_id:
                if resource[1].test() == True:
                    return False

                else:
                    if self.locks <= self.Y:
                            self.locks += 1
                            status = resource[1].lock(client_id, time_limit)
                            if status == "Unavailable":
                                resource[1].disable()
                                return "Unavailable"
                            else:
                                return status

                    else:
                            return False
        return False

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """

        for resource in self.lock_array:
            if resource[0] == resource_id:
                if resource[1].release(client_id):
                    self.locks -= 1
                    return True
                else:
                    return False

    def test(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado False caso
        esteja desbloqueado ou inativo.
        """
        for resource in self.lock_array:
            if resource[0] == resource_id:
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

        for resource in self.lock_array:
            if resource[1].test() == True:
                clients = " " + str(resource[1].client) + " "
                print resource[1].time
                output += ("Recurso ID: " + str(
                    resource[0]) + " bloqueado pelo(s) o cliente(s):" + clients + " até aos " + str(
                    resource[1].time_limit) + " Segundos, Tempo passado: " + str(
                    time.time() - resource[1].time) + " Segundos\n")

            elif resource[1].test() == "Unavailable":
                if resource[0] == 0:
                    output += "\nRecurso ID: " + str(resource[0]) + " inativo  \n"
                else:
                    output += "Recurso ID: " + str(resource[0]) + " inativo \n"

            elif resource[1].test() == False:
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
