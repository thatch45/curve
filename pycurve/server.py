'''
Set up the server daemon
'''
# Import python libs
import socket


class Server(object):
    def __init__(self, opts):
        self.opts = opts

    def bind(self):
        '''
        Bind to the given udp port
        '''
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.bind((self.opts['server_ip'], self.opts['server_port']))
        while True:
            data, addr = sock.recvfrom(1024)
            # Deal with data here
