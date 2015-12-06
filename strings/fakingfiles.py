'''
Created on Dec 5, 2015

@author: Sameer Adhikari
'''

# coding = utf-8

from io import BytesIO, StringIO

fake_source_file = StringIO("an oft-repeated cliché")
fake_destination_file = BytesIO()

char = fake_source_file.read(1)
while char:
    fake_destination_file.write(char.encode('ascii', 'replace'))
    char = fake_source_file.read(1)

print(fake_destination_file.getvalue())

    