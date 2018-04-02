# coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - net_client.py
Grupo: ad001
Números de aluno: 48314 | 48292 | 48299

"""

# zona para fazer importação

from sock_utils import create_tcp_client_socket

# definição da classe server

class server:
    """
    Classe para abstrair uma ligação a um servidor TCP. Implementa métodos
    para estabelecer a ligação, para envio de um comando e receção da resposta,
    e para terminar a ligação
    """

    def __init__(self, address, port):
        """
        Inicializa a classe com parâmetros para funcionamento futuro.
        """
        self.address = address
        self.port = port
        self.client_sock = create_tcp_client_socket(address, port)

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        self.client_sock.connect((self.address, int(self.port)))

    def send_receive(self, socket, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """
        socket.sendall(data)
        return socket.recv(1024)

    def close(self, socket):
        """
        Termina a ligação ao servidor.
        """
        socket.close()
