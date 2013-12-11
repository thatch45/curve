'''
Set up the server daemon
'''
# Import python libs
import socket
import time
import json

class Handler(object):
    def __init__(self, opts, data):
        self.opts = opts
        self.data = data

    def handle_data(self):
        '''
        Handle the data sent from a client
        '''
        ret = json.dumps({'track': self.data['track']})
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(ret, (self.data['ret_ip'], self.data['ret_port']))


class Server(object):
    def __init__(self, opts, ip=None, port=None):
        self.opts = opts
        self.sock = self.__bind(ip, port)

    def __bind(self, ip, port):
        '''
        Bind to the given udp port
        '''
        if ip is None:
            ip = self.opts['server_ip']
        if port is None:
            port = self.opts['server_port']
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.settimeout(self.opts.get('server_timeout', 0.1))
        sock.bind((ip, port))
        return sock

    def serv(self):
        '''
        Start handling all incoming information
        '''
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
            except Exception:
                pass
            if data and addr:
                # Handle the data
                data = json.loads(data)
                handler = Handler(self.opts, data)
                handler.handle_data()

    def recv_iter(self, timeout=1):
        '''
        Forever yield returns as they come
        '''
        start = time.time()
        while True:
            try:
                data, attr = self.sock.recvfrom(1024)
                yield data, attr
            except socket.timeout:
                pass
            if start + timeout < time.time():
                break
        yield None, None

    def recv_timeout(self, timeout=1):
        '''
        Wait for the timeout for the return else return None
        '''
        for data, addr in self.recv_iter(timeout):
            return data, addr
