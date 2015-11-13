'''
Created on Nov 6, 2015

@author: Sameer Adhikari
'''

import argparse
import socket

class EchoSocket:
    '''
    Decorator that adds echoing capabilities to the socket class.
    Technically, this should implement all the methods of socket.
    The send method should have all the optional parameters.
    But, comprehensiveness is not a goal of this example.
    '''
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print('Sending to destination: {0}, data = {1}'.format(self.socket.getpeername()[0], data))
        
    def close(self):
        self.socket.close()

class Server:
    '''
    '''
    def __init__(self, echo=False):
        self.echo = echo
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 2401))
        self.server.listen(1)
        
    def respond(self, client):
        response = input("Enter an integer value to send to client: ")
        client.send(bytes(response))
        client.close()
        
    def run(self):
        try:
            while True:
                client, add = self.server.accept()
                if self.echo:
                    client = EchoSocket(client)
                self.respond(client)
        finally:
            self.server.close()
                
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--echo', type=bool, default=False, help = 'whether to echo the send on the terminal')
    args = parser.parse_args()
    server = Server(args.echo)
    server.run()
    