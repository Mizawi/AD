#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicações distribuídas - Projeto 1 - lock_skel.py
Grupo: ad001
Números de aluno: 48314 | 48299 | 48292
"""

# Zona para fazer imports
import lock_pool as lpool
import pickle as p
from pprint import PrettyPrinter

pp = PrettyPrinter()

class LockSkel:

    def __init__(self, N, K, Y, T):
        self.lp = lpool.lock_pool(N, K, Y, T)

    def msgreceiver(self, msg, argv):


        # Commando Lock
        if 10 == msg[0]:
            estado = self.lp.lock(int(msg[1]), int(msg[2]), int(argv[5]))
            if estado == True:
                answer = p.dumps([11, "True"], -1)
            elif estado == "Unavailable":
                answer = p.dumps([11, "Disable"], -1)
            else:
                answer = p.dumps([11, "False"], -1)

        # Comando Release
        elif 20 == msg[0]:
            estado = self.lp.release(int(msg[1]), int(msg[2]))
            if estado == True:
                answer = p.dumps([21, "True"], -1)
            else:
                answer = p.dumps([21, "False"], -1)

        # Comando Test
        elif 30 == msg[0]:
            estado = self.lp.test(int(msg[1]))
            if estado == True:
                answer = p.dumps([31, "True"], -1)
            elif estado == "Unavailable":
                answer = p.dumps([31, "Disable"], -1)
            else:
                answer = p.dumps([31, "False"], -1)
        # Comando Stats
        elif 40 == msg[0]:
            if int(self.lp.stat(int(msg[len(msg) - 1]))) > 0:
                answer = p.dumps([41, str(self.lp.stat(int(msg[len(msg) - 1])))], -1)
            else:
                answer = p.dumps([41, "None"], -1)

        # Comando Stats_Y
        elif 50 == msg[0]:
            answer = p.dumps([51, str(self.lp.stat_y())], -1)

        # Comando Stats_N
        elif 60 == msg[0]:
            answer = p.dumps([61, str(self.lp.stat_n())], -1)

        elif 00 == msg[0]:
            answer = p.dumps([01, "Conexão Encerrada"], -1)

        else:
            answer = p.dumps([404, "UNKNOWN COMMAND"], -1)

        return answer