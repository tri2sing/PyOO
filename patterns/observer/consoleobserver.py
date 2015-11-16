'''
Created on Nov 15, 2015

@author: Sameer Adhikari
'''
from patterns.observer.subject import Subject

class ConsoleObserver:
    def __init__(self, subject):
        self.subject = subject
        
    def __call__(self):
        print('Observer notified')
        print('New data = {}'.format(self.subject.data))
        
if __name__ == '__main__':
    subject = Subject()
    consobs = ConsoleObserver(subject)
    subject.attach(consobs)
    print('Current subject data = {}'.format(subject.data))
    print('Now manipulating the subject')
    subject.data = 5 #Some entity manipulates the subject