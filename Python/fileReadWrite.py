__author__ = 'warrickmoran'
#
# General Read/Write methods from Python 101
#

def file_read(filename):
    """
    Read File Contents
    """
    try:
        with open(filename, 'r') as handler:
            data = handler.readlines() # read ALL the lines!
            print(data)
    except IOError:
        print("An IOError has occurred!")


def file_write(filename):
    """
    Write File
    """
    try:
        with open(filename,'w') as handler:
            handler.write("This is a test!")
    except IOError:
        print("An IOError has occurred!")


file_read('data/text.txt')
file_write('data/output.txt')
