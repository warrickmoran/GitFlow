__author__ = 'warrickmoran'

def fileRead():
    handler = open('data/text.txt', 'r')
    data = handler.readlines() # read ALL the lines!
    print(data)
    handler.close()

def fileWrite():
    handler = open('data/output.txt','w')
    handler.write("This is a test!")
    handler.close()

fileRead()
fileWrite()