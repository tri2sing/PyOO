'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

from patterns.adapter.cat import Cat
from patterns.adapter.dog import Dog
from patterns.adapter.person import Person
from patterns.adapter.dogadapter import DogAdapter
from patterns.adapter.creatureadapter import CreaturAdapter


def test_specific_adapter():
    person = Person('Jane Doe')
    canine = DogAdapter(Dog('Fido'))
    for creature in (person, canine):
        print('{} emits {}'.format(creature.name, creature.make_noise()))

    
def test_generic_adapter():
    person = Person('Sunny')
    salty = Dog('Salty')
    saucy = Cat('Saucy')
    canine = CreaturAdapter(salty, salty.bark)
    feline = CreaturAdapter(saucy, saucy.meow)
    for creature in (person, canine, feline):
        print('{} emits {}'.format(creature.name, creature.make_noise()))


if __name__ == '__main__':
    print(8*'=' + ' SPECIFIC ADAPTER ' + 8*'=')
    test_specific_adapter()
    print(8*'=' + ' GENERIC ADAPTER ' + 8*'=')
    test_generic_adapter()
    