## FUNCTIONS
# function syntax:
# def function_name(parameters):
def greeting(name):
    print("Hello", name)
    # functions can use the global scope
    print(greeter)

greeter = "Simon"
greeting("Peter")

greeter = "Ann"
greeting("Peter")

# functions can return values
def add(num1, num2):
    return num1 + num2

print(add(2, 2))

# functions can return multiple values
# note this returns a tuple which we can index as seen already
def square_and_cube(a):
    return a**2, a**3 

square_and_cube(3)

# functions with optional arguments
def room_checker(day, num_people, video=False, duration=1):
    if(video):
        print("We have {0} rooms available with video conferencing on {1} for {2} people lasting {3} hours".format(2, day, num_people, duration))
    else:
        print("We have {0} rooms available without video conferencing on {1} for {2} people lasting {3} hours".format(4, day, num_people, duration))


# we can call functions using the argument names themselves (keyword arguments)
# note the optional arguments were not provided
room_checker(day="Thursday", num_people=7)

# passing all arguments
room_checker(day="Thursday", num_people=7, video=True, duration=3)

# mix/match names and positions
room_checker("Thursday", num_people=7, duration=3)

# BUT! Positional arguments must appear before keyword arguments
# room_checker(day="Thursday", 7, duration=3)   # this doesn't work

# *args - to accept an arbitrary number of arguments
def how_many_args(*args):
    print("You passed {0} arguments".format(len(args)))
    print(type(args))

how_many_args(1, 2, 3, 4, 5)

# it is common to mix star args with normal args BUT star args must come after
# also the name *args is just a convention
def how_many_args_with_length(length, *num_args):
    print("Your length is {0} arguments but we calculated {1}".format(length, len(num_args)))
    print(type(num_args))

how_many_args_with_length(4, 1, 2, 3, 4, 5)

# **kwargs - to accept an arbitrary number of keyword arguments
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

tag("img", src="home.jpg", alt="My house", border=1)

# functions can return functions i.e. first class functions (functional programming)
def add_five():
    def add(num):
        return num + 5

    return add

adder = add_five()
print(adder(5))

# and functions can be stored as variables and passed around
def map(collection, f):
    return [f(x) for x in collection]

# note without the parentheses as this calls the function
m = map
type(m)

m([1.231, 2.233, -4.45454, -454.454, 34.34], abs)
m([1.231, 2.233, -4.45454, -454.454, 34.34], int)