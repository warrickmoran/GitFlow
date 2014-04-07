__author__ = 'warrickmoran'

def fileRead():
    handler = open('data/text.txt', 'r')
    data = handler.readlines() # read ALL the lines!
    print(data)
    handler.close()


fileRead()