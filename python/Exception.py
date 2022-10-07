
# //* ---------Try ,Except, Else , Finally----------//

from sys import exc_info


def div(a,b):
    # if b == 0:
    #     raise Exception("ZEro Devision Error")

    try :
        z = a/b
    except ZeroDivisionError:
        print('Cant Devide By Zero')

    else:
        print(z)

    finally:
        print('Program Completed')

# div(1,2)


# //*------Throwing An Error By Raise Keyword-----------//

def age(a):
    if a < 18:
        raise Exception("Age is Less Than 18")

# age(12)

# //*----------Assertion Method-------//

def phn(a):
    a = str(a)
    assert len(a) ==10 , "Phone Number Has to be of 10 Digits"

# phn(770993129)


# //*---Multiple Error to be Handle--*//

import sys
def devision(a,b):

    try :
        z = a/b
    # except sys.exc_info()[0]:
    #     print('got Zero Devision')
    
    except TypeError:
        print('Type OF Error is',sys.exc_info()[0])
        print(' Error is',sys.exc_info()[1])
        print(' Error Object is',sys.exc_info()[2])

    except ZeroDivisionError:
        ertuplt = sys.exc_info()
        print(ertuplt)

    else:
        print(z)

devision(10,0)