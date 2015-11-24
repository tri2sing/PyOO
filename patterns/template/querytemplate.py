'''
Created on Nov 23, 2015

@author: Sameer Adhikari
'''
import sqlite3

class QueryTemplate(object):
    def connect(self):
        self.connection = sqlite3.connect('sales.db')
    
    def construct_query(self):
        raise NotImplementedError()

    def execute_query(self):
        results = self.connection.execute(self.query)
        self.results = results.fetchall()
        
    def format_results(self):
        output = []
        for row in self.results:
            row = [str(term) for term in row]
            output.append(','.join(row))
        self.formatted_results = '\n'.join(output)
        
    def output_results(self):
        raise NotImplementedError()
    
    def process(self):
        self.connect()
        self.construct_query()
        self.execute_query()
        self.format_results()
        self.output_results()