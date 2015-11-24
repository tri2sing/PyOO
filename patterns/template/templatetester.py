'''
Created on Nov 23, 2015

@author: Sameer Adhikari
'''
from patterns.template.newvehiclesquery import NewVehiclesQuery
from patterns.template.salespersonquery import SalesPersonQuery

if __name__ == '__main__':
    newvehicles = NewVehiclesQuery()
    salespersons = SalesPersonQuery()
    newvehicles.process()
    salespersons.process()