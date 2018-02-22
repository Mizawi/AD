#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
"""

# Zona de importacao

import socket as s


################################################

def create_tcp_server_socket(address, port, queue_size):
    """
    Cria uma socket do tipo TCP para ser usadat como Servidor

    :param str address:
    :param int port:
    :param int queue_size:
    :return socket sock:
    """
    host = address
    port = int(port)

    sock = s.socket(s.AF_INET, s.SOCK_STREAM, s.IPPROTO_TCP)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

    sock.bind((host, port))
    sock.listen(int(queue_size))

    return sock


def create_tcp_client_socket(address, port):
    """
    Cria uma socket do tipo TCP para ser usada como Cliente

    :param str address:
    :param int port:
    :return socket sock:
    """
    host = address
    port = port

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)

    sock.connect((host, int(port)))

    return sock


def receive_all(socket, length):
    """
    Retorna os dados a receber de tamanho length, caso passado 10000 segundos manda mensagem a dizer "Nao recebi dados"

    :param socket socket:
    :param int length:
    :return socket.recv(lenght):
    """
    socket.settimeout(10000)
    try:
        return socket.recv(length)
    except socket.timeout() as socket:
        socket.timeout(None)
        socket.sendall("Nao recebi dados")
