# Maths - basic arithmetic module
# demonstrates Python modules to maintain cleaner code

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

# modules can even be executed in their own right
# to do this they need an entry point:
# this is an example of a "Python Magic Method" (or Dunder method, double underscore) which start/end with double underscores
# they are special built-in methods that are called by Python at certain points which we 
# can hook onto to perform various tasks
# Here we grab the magic method __name__, if this is set to __main__ then we know that 
# this module was executed as the main program e.g. python .\maths\arithmetic.py
# otherwise __name__ is the name of the module i.e. arithmetic
#
# Note the appearance of the __pycache__ folder in the module folder
# Python caches the "compiled" version of every module to speed up module loading
# The contents are the byte code which the Python interpreter "compiles" to. This byte 
# code is what the Python Virtual machine executes. This blurs the line between what I said 
# earlier about Python being an interpreted language, but without getting too technical, the 
# byte code is just instructions for a virtual machine, not native machine instructions, hence 
# we class it as an interpreted language.
if __name__ == "__main__":
    print("Running the arithmetic module directly as a script!")
    res = add(1, 1) + multiply(2, 2) + subtract (3, 1) + divide(10, 5)
    print(res)
