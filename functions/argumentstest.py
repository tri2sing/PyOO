'''
Created on Oct 22, 2015

@author: Sameer Adhikari
'''

import datetime

from functions.arguments import Timer

def format_time(message, *args):
    now = datetime.datetime.now().strftime('%I:%M:%S')
    print(message.format(*args, now=now))
    
def one(timer):
    format_time('{now}: Called one')
    print('Used {} in one'.format(timer))
    
def two(timer):
    format_time('{now}: Called two')
    print('Used {} in two'.format(timer))
    
def three(timer):
    format_time('{now}: Called three')
    print('Used {} in three'.format(timer))
    
class Repeater:
    def __init__(self):
        self.count = 0
        
    def repeater(self, timer):
        format_time('{now}: repeat {0} in repeater', self.count)
        print('Used {} in repeater'.format(timer))
        self.count += 1
        # Recursively add events to the timer
        timer.add_event(self.repeater, 5)
        
timer = Timer()
print('Created {}'.format(timer))
# At this point we are not passing a timer argument to the callback function.
# The timer instances get sent as an argument only at the callback invocation.
timer.add_event(one, 1)
timer.add_event(one, 2)
timer.add_event(two, 2)
timer.add_event(two, 4)
timer.add_event(three, 3)
timer.add_event(three, 6)

repeater = Repeater()
timer.add_event(repeater.repeater, 5)
format_time('{now}: Starting')
timer.run()

