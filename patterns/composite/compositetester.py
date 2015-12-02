'''
Created on Dec 2, 2015

@author: Sameer Adhikari
'''


from patterns.composite.entities import root, Folder, File

if __name__ == '__main__':
    folder1 = Folder('folder1')
    folder2 = Folder('folder2')
    root.add_child(folder1)
    root.add_child(folder2)
    folder11 = Folder('folder11')
    folder1.add_child(folder11)
    file111 = File('file111', 'contents')
    folder11.add_child(file111)
    file21 = File('file21', 'other contents')
    folder2.add_child(file21)
    print(folder2.children)
    folder2.move('/folder1/folder11')
    print(folder11.children)
    file21.move('/folder1')
    print(folder1.children)    