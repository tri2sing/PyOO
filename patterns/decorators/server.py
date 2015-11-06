'''
Created on Nov 6, 2015

@author: Sameer Adhikari
'''

import socket

class Server:
    '''
    '''
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 2401))
        self.server.listen(1)
        
    def respond(self, client):
        response = input("Enter a value to send to client: ")
        client.send(bytes(response))
        client.close()
        
    def run(self):
        try:
            while True:
                client, add = self.server.accept()
                self.respond(client)
        finally:
            self.server.close()
                
    
if __name__ == '__main__':
    server = Server()
    server.run()
    