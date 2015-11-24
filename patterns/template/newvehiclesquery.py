'''
Created on Nov 23, 2015

@author: Sameer Adhikari
'''
from patterns.template.querytemplate import QueryTemplate

class NewVehiclesQuery(QueryTemplate):
    '''
    Class that uses the template base class to do most of its work.
    '''
    
    def construct_query(self):
        self.query = "select * from Sales where new='true'"
        
    def output_results(self):
        print(self.formatted_results)   