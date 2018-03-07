# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - net_client.py
Grupo:
Números de aluno:
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
        pass # Remover esta linha e fazer implementação da função
        
    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        pass # Remover esta linha e fazer implementação da função

    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """
        pass # Remover esta linha e fazer implementação da função
    
    def close(self):
        """
        Termina a ligação ao servidor.
        """
        pass # Remover esta linha e fazer implementação da função
