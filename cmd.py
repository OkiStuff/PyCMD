import os
import color



def init():

    print(str(color.prYellow("PyCMD v1.0 by Okistuff") ))
        

def catch_error(e):

    print(str(color.prRed("ERROR: " + str(e) )) )
    exit()


def commands(s):

    try:

        os.system(s)

    except Exception as error:

        catch_error(error)

def get_commands():
    try:

        c = input(str(color.prCyan("> ") ) )

        commands(c)

    except Exception as error:

        catch_error(error)

init()


while True:

    get_commands()