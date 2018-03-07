import socket as s
from multiprocessing import Process


def create_tcp_server_socket(address, port, queue_size):
    """Creates a server socket"""

    sock = s.socket(s.AF_INET, s.SOCK_STREAM,)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((address, int(port)))
    sock.listen(queue_size)

    return sock

def create_tcp_client_socket(address, port):
    """Creates a client socket"""

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((address, int(port)))

    return sock


def receive_all(socket, length):
    """Data transmitter"""

    msg = socket.recv(length)
    return msg

