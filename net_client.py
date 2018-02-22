#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 09
Números de aluno: 48314 | 48299 | 48292
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

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        return create_tcp_client_socket(self.address, self.port)

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