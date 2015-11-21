'''
Created on Nov 20, 2015

@author: Sameer Adhikari
'''

def odd_series_generator(limit):
    return [x for x in range(1, limit) if x%2 != 0]
    
def even_series_generator(limit):
    return [x for x in range(1, limit) if x%2 == 0]
    
def fibonacci_series_generator(limit):
    series = []
    f0 = 0
    if f0 < limit: 
        series.append(f0) 
    f1 = 1
    if f1 < limit:
        series.append(f1)
    f2 = f0 + f1
    while f2 < limit:
        series.append(f2)
        f0 = f1
        f1 = f2
        f2 = f0 + f1
    
    return series
        