__author__ = 'warrickmoran'

def fileRead():
    """
    Read File Contents
    """
    try:
        with open('data/text.txt', 'r') as handler:
            data = handler.readlines() # read ALL the lines!
            print(data)
    except IOError:
        print("An IOError has occurred!")


def fileWrite():
    try:
        with open('data/output.txt','w') as handler:
            handler.write("This is a test!")
    except IOError:
        print("An IOError has occurred!")


fileRead()
fileWrite()