'''
Created on Oct 22, 2015

@author: Sameer Adhikari
'''


import datetime
import time

class TimedEvent:
    '''
    TimedEvent class is not meant to be accessed by other classes.
    The goal is to demonstrate passing functions as arguments
    '''
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback
        
    def ready(self):
        return self.endtime <= datetime.datetime.now()
    
class Timer:
    '''
    Class that stores a list of upcoming events and processes them.
    '''
    def __init__(self):
        self.events = []
        
    def add_event(self, callback, delaysec):
        '''
        callback: function with time argument to invoke when event is ready to run.
        delaysec: delay in seconds after which the event fires.
        '''
        # Check if the argument callback is callable 
        if not hasattr(callback, '__call__'):
            raise TypeError('{} is not callable'.format(callback))
        
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delaysec)
        self.events.append(TimedEvent(end_time, callback))
    
    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                # Pass the timer to the callback function as an argument
                event.callback(self)
                self.events.remove(event)
            time.sleep(1)
            
            
                
                    
