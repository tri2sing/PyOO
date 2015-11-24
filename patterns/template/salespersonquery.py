'''
Created on Nov 23, 2015

@author: Sameer Adhikari
'''
from patterns.template.querytemplate import QueryTemplate

class SalesPersonQuery(QueryTemplate):
    '''
    Class that uses the template base class to do most of its work.
    '''
    
    def construct_query(self):
        self.query = "select salesperson, sum(amount) from Sales group by salesperson"
        
    def output_results(self):
        with open('salesperson_amount.txt', 'w') as f:
            f.write(self.formatted_results)
