# how to import and use modules
# When the interpreter sees an import it searches for maths/arithmetic.py in a list of directories:
# Firstly from the directory the input script is run, or the current directory if the interpreter is being run interactively.
# A list of directories specified in the PYTHONPATH environment variable, like the PATH environment variable, contains a list of directories. Doesn't have to be set.
# Then a default list of directories configured at the time Python was installed.

# It's quite easy to import, but you can get into a muddle, especially with relative imports from sub-folders
# If your imports aren't working then you can check where the interpreter is looking via the sys module's path property:
# (If you want a brute-force approach, you can put the module anywhere and then modify sys.path at run-time so it's picked up).
# import sys
# print(sys.path)

# importing our maths/arithmetic.py module
# import maths.arithmetic
# print(maths.arithmetic.add(2, 3))

# you can check exactly where a module came from using the __file__ magic method:
# (can be useful when debuggin import problems)
# print(maths.arithmetic.__file__)

# importing using an alias
# import maths.arithmetic as yo
# print(yo.add(3, 3))

# import using 'from' as a cleaner way
from maths import arithmetic
print(arithmetic.add(4, 3))

# wildcard import to import everything (discouraged)
# from maths.arithmetic import *
# print(add(5, 3))
