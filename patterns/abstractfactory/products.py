'''
Created on Nov 30, 2015

@author: Sameer Adhikari
'''

import abc

class AbstractDateFormatter(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def format_date(self, year, month, day):
        ''' Sub class has to implement this function '''


class FranceDateFormatter(AbstractDateFormatter):
    def format_date(self, year, month, day):
        y, m, d = (str(k) for k in (year, month, day))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return '{0}/{1}/{2}'.format(d, m, y)


class USADateFormatter(AbstractDateFormatter):
    def format_date(self, year, month, day):
        y, m, d = (str(k) for k in (year, month, day))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return '{0}-{1}-{2}'.format(m, d, y)

        
class AbstractCurrencyFormatter(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def format_currency(self, base, cents):
        ''' Sub class has to implement this function '''


class FranceCurrencyFormatter(AbstractCurrencyFormatter):
    def format_currency(self, base, cents):
        base, cents = (str(k) for k in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        
        
        digits = []
        for i, d in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(d)
            
        base = ''.join(reversed(digits))
        return '{0}€{1}'.format(base, cents)

class USACurrencyFormatter(AbstractCurrencyFormatter):
    def format_currency(self, base, cents):
        base, cents = (str(k) for k in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        
        
        digits = []
        for i, d in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(',')
            digits.append(d)
            
        base = ''.join(reversed(digits))
        return '${0}.{1}'.format(base, cents)
    
    
    
if __name__ == '__main__':
    frdate = FranceDateFormatter()
    print(frdate.format_date(15, 9, 25))
    frcurr = FranceCurrencyFormatter()
    print(frcurr.format_currency(1500, 50))
    
    usdate = USADateFormatter()
    print(usdate.format_date(15, 9, 25))
    usacurr = USACurrencyFormatter()
    print(usacurr.format_currency(1400, 39))

                    
        