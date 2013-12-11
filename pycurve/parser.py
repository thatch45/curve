'''
Parse command line options
'''

import optparse


def parse():
    '''
    Parse options for a server
    '''
    parser = optparse.OptionParser()
    parser.add_option(
            '--server-ip',
            dest='server_ip',
            default='127.0.0.1',
            help='the server ip')
    parser.add_option(
            '--server-port',
            dest='server_port',
            default='4510',
            help='the server port')
    parser.add_option(
            '-m',
            '--message',
            dest='message',
            default='foo',
            help='The message to send')

    options, args = parser.parse_args()
    return options.__dict__