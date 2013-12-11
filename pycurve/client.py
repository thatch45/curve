'''
Set up the client end
'''

# Import python libs
import socket

class Client(object):
    def __init__(self, opts):
        self.opts = opts

    def send(self, msg):
        '''
        '''
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(msg, (self.opts['server_ip'], self.opts['server_port']))
