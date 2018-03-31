#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicações distribuídas - Projeto 1 - lock_skel.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
"""


# Zona para fazer imports

import lock_pool as l
import pickle as p
from pprint import PrettyPrinter

pp = PrettyPrinter()

class LockSkel:

    def __init__(self, N, K):
        self.lp = l.lock_pool(N, K)


    def msgreceiver(self, msg, argv):

        pp.pprint(msg)
        if int(msg[len(msg) - 1]) > (int(argv[2]) - 1):
            answer = p.dumps([int(msg[0])+1, "None"], -1)

        # Commando Lock
        elif 10 == msg[0]:
            Estado = self.lp.lock(int(msg[2]), int(msg[1]), int(argv[4]))
            if Estado == True:
                answer = p.dumps([11, "OK"], -1)
            else:
                answer = p.dumps([11, "NOK"], -1)

        # Comando Release
        elif 20 == msg[0]:
            Estado = self.lp.release(int(msg[2]), int(msg[1]))
            if Estado == True:
                print "Resource: ", msg[2], "Released"
                answer = p.dumps([21, "OK"], -1)
            else:
                answer = p.dumps([21, "NOK"], -1)

        # Comando Test
        elif 30 == msg[0]:
            Estado = self.lp.test(int(msg[len(msg) - 1]))
            if Estado == True:
                answer = p.dumps([31, "LOCKED"], -1)
            else:
                answer = p.dumps([31, "NOT LOCKED"], -1)
        # Comando Stats
        elif 40 == msg[0]:
            if str(self.lp.stat(int(msg[len(msg) - 1]))) > 0:
                answer = p.dumps([41, str(self.lp.stat(int(msg[len(msg) - 1])))], -1)
            else:
                answer = p.dumps([31, "None"], -1)

        # Comando Stats_k
        elif 50 == msg[0]:
            answer = p.dumps([51, str(self.lp.stat_y())], -1)

        elif 60 == msg[0]:
            answer = p.dumps([61, str(self.lp.stat_n())], -1)

        elif 00 == msg[0]:
            answer = p.dumps([01, "Conexão Encerrada"], -1)

        else:
            answer = p.dumps([404, "UNKNOWN COMMAND"], -1)

        return answer