'''
Set up the client end
'''
# Import pycurve libs
import pycurve.server

# Import python libs
import socket
import json
import time

class Client(object):
    def __init__(self, opts):
        self.opts = opts
        self.retserv = pycurve.server.Server(
                self.opts,
                self.opts['ret_ip'],
                self.opts['ret_port'])
        self.retserv.bind()

    def send(self, body):
        '''
        '''
        payload = json.dumps(
                {'body': body,
                 'ret': ''}
                )
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(payload, (self.opts['server_ip'], self.opts['server_port']))

    def send_recv(self, body, timeout=5):
        '''
        Block for a return, classic rep/req
        '''
        track = int(time.time()*1000000)
        payload = json.dumps({
                 'body': body,
                 'cmd': 'command',
                 'ret_ip': self.opts['ret_ip'],
                 'ret_port': self.opts['ret_port'],
                 'track': track
                 })
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(payload, (self.opts['server_ip'], self.opts['server_port']))
        return self.retserv.recv_timeout(timeout)
