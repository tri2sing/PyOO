'''
Created on Nov 6, 2015

@author: Sameer Adhikari
'''

import socket

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def communicate(self):
        self.client.connect(('localhost', 2401))
        print('Received: {0}'.format(self.client.recv(1024)))
        self.client.close()
        

if __name__ == '__main__':
    client = Client()
    client.communicate()