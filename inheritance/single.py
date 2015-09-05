'''
Created on Sep 4, 2015

@author: Sameer Adhikari
'''

class Contact(object):

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    
    def order(self, order=''):
        print('oder = {}, buyer = {}'.format(order, self.name))

class Friend(Contact):
    def __init__(self, name, email, phone):
        #super().__init__(name, email)
        Contact.__init__(self, name, email)
        self.phone = phone
            
c = Contact('jane doe', 'janedoe@buyer.net')
s = Supplier('john doe', 'johndoe@supplier.com')
f = Friend('jill smith', 'jillsmith@friend.org', '999-999-9999')

print(c)
print(s)
print(f)
print(Contact.all_contacts)
s.order('order 1')

# c.order('order 2')
