# coding=utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket as s

"""
Aplicações distribuídas - Projeto 1 - sock_utils.py
Grupo: 01
Números de aluno: 48314 | 48292 | 48299

"""


def create_tcp_server_socket(address, port, queue_size):
    """
    Cria uma socket do tipo TCP para ser usada como Servidor
    :param str adress:
    :param int port:
    :return socket sock:
    """
    host = address
    port = int(port)

    sock = s.socket(s.AF_INET, s.SOCK_STREAM, s.IPPROTO_TCP)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(queue_size)

    return sock


def create_tcp_client_socket(address, port):
    """
    Cria uma socket do tipo TCP para ser usada como Client
    :param str address:
    :param int port:
    :return socket sock:
    """

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)


    return sock


def receive_all(socket, length):
    """Retorna os dados a receber de tamanho length, caso passado 10000
    segundos manda mensagem a dizer "Não recebi dados"

    :param socket socket:
    :param int length:
    :return socket.recv(length):
    """

    socket.settimeout(10000)
    try:
        return socket.recv(length)
    except socket.timeout() as socket:
        socket.timeout(None)
        socket.sendall("Nao recebi dados")
