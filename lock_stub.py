#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Aplicações distribuídas - Projeto 1 - lock_stub.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
"""
from net_client import server

import pickle as p


class LockStub:
    def __init__(self, address, port):
        self.netclient = server(address, port)
        self.netclient.connect()

    def lock(self, msg):
        cmd = p.dumps([10, msg[0], msg[1]], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def release(self, msg):
        cmd = p.dumps([20, msg[0], msg[1]], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def test(self, msg):
        cmd = p.dumps([30, msg[0]], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def stats(self, msg):
        cmd = p.dumps([40, msg[0]], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def stats_y(self):
        cmd = p.dumps([50], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def stats_n(self):
        cmd = p.dumps([60], -1)

        return self.netclient.send_receive(self.netclient.client_sock, cmd)

    def close(self):
        cmd = p.dumps([00], -1)
        self.netclient.send_receive(self.netclient.client_sock, cmd)
        self.netclient.client_sock.close()