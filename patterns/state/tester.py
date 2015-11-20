'''
Created on Nov 19, 2015

@author: Sameer Adhikari
'''

import patterns.state.parser as psr

import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        contents = file.read()
        print(contents)
        parser = psr.Parser(contents)
        parser.start()
        
        print(64*'=')
        nodes = [parser.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes
