'''
Created on Dec 1, 2015

@author: Sameer Adhikari
'''

import random
from patterns.abstractfactory.factories import \
    USAFormatterFactory, FranceFormatterFactory

factory_map = {
    'US': USAFormatterFactory,
    'FR': FranceFormatterFactory
    }

# We use a random number generator to choose the factory.
# In reality, we would read the locale and decide.
random.seed()
val = random.choice([0, 1])
if val == 0:
    code = 'FR'
else:
    code = 'US'   

# Create a module variable to mimic a singleton
factory = factory_map[code]()