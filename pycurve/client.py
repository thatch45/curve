'''
Set up the client end
'''

# Import python libs
import socket
import json

class Client(object):
    def __init__(self, opts):
        self.opts = opts

    def send(self, body):
        '''
        '''
        payload = json.dumpd(
                {'body': body,
                  'ret': ''}
                )
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(payload, (self.opts['server_ip'], self.opts['server_port']))
