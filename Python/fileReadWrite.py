__author__ = 'warrickmoran'

def file_read():
    handler = open('data/text.txt', 'r')
    data = handler.readlines() # read ALL the lines!
    print(data)
    handler.close()

def file_write():
    handler = open('data/output.txt','w')
    handler.write("This is a test!")
    handler.close()

file_read()
file_write()