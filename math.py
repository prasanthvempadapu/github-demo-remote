#add implementation
def add(x,y):
    return x+y
#substract implementations 
def substract(x,y):
    return x-y                  #on master branch
#multiply implementation
def multiply(x,y):
    return x*y                #on Bug456
#divide implementation
def divide(x,y):
    if y==0:
        return DIVIDE_ZERO-ERROR
    else:
        return x/y
#square implementation
def square(x):
    return x*x