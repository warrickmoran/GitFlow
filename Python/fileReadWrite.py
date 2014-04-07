__author__ = 'warrickmoran'


def file_read():
    """
    Read File Contents
    """
    try:
        with open('data/text.txt', 'r') as handler:
            data = handler.readlines() # read ALL the lines!
            print(data)
    except IOError:
        print("An IOError has occurred!")


def file_write():
    """
    Write File
    """
    try:
        with open('data/output.txt','w') as handler:
            handler.write("This is a test!")
    except IOError:
        print("An IOError has occurred!")

if __name__ == '__main__':
    file_read()
    file_write()
