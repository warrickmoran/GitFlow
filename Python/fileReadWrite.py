__author__ = 'warrickmoran'

def fileRead():
    """
    Read File Contents
    """
    try:
        handler = open('data/text.txt', 'r')
        data = handler.readlines() # read ALL the lines!
        print(data)
    except IOError:
        print("An IOError has occurred!")
    finally:
        handler.close()

def fileWrite():
    try:
        handler = open('data/output.txt','w')
        handler.write("This is a test!")
    except IOError:
        print("An IOError has occurred!")
    finally:
        handler.close()

fileRead()
fileWrite()