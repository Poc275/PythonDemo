import random

class Person:
    # constructors are defined by another "magic method" __init__
    # self is a special keyword referring to a particular instance of the class
    def __init__(self, first_name, surname, age):
        # instance variables
        # self._first_name = first_name
        # now we have properties it is a good idea to use them internally  
        # this way we're encapsulating the logic all together and if our setters contained  
        # complex logic, we get this for free during instantiation
        self.first_name = first_name
        self.surname = surname
        self.age = age

    # Properties
    # Python doesn't have getters/setters like in other OO languages Java/C#
    # The @property decorator lets us call first_name as a property instead of a method call, aka a getter
    @property
    def first_name(self):
        return self._first_name

    # for setters we need to use the getter property and extend it .setter
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 18 or value > 80:
            raise ValueError("Invalid age!")

        self._age = value

    # instance method example
    def to_string(self):
        print("{0} {1} is {2}".format(self.first_name, self.surname, self.age))

    # class method example - class methods take a cls parameter which is the Person class
    # class methods can be useful particularly in a Factory pattern where we call a factory 
    # method to generate an instance instead of calling a constructor directly. The class 
    # object cls lets us create a new instance:
    @classmethod
    def create_random_person(cls):
        first_name = random.choice(['Helen', 'John', 'Ann', 'Steve'])
        surname = random.choice(['Smith', 'Jones'])
        age = random.randint(18, 80)
        return cls(first_name, surname, age)


# inheritance example
class Staff(Person):
    # class variables - shared by all instances of Staff
    next_staff_id = 1

    def __init__(self, first_name, surname, age):
        # note that Python DOESN'T call base class constructors automatically like other OO languages, 
        # you have to call them explicitly (explicit is better than implicit > Zen of Python)
        super().__init__(first_name, surname, age)
        self._staff_id = Staff._generate_staff_id()

    # static method example, static methods/variables don't need a particular instance
    # so there's no self parameter
    # @staticmethod is an example of a "decorator" - Python decorators wrap a function 
    # modifying its behaviour, here @staticmethod modifies _generate_staff_id so it can be 
    # called on uninstantiated objects, like static in Java/C#
    #
    # There are also class methods in Python marked with the @classmethod decorator
    # Class methods have access to the underlying class, not a particular instance (self)
    # whereas static methods don't have access to either. (Some argue that because static 
    # methods don't need access to anything within the class, they should be moved elsewhere.)
    # See Person class for an example of class methods.
    #
    # Note Python doesn't have public/private modifiers so it is convention to prefix 
    # with an underscore for private methods/variables, although there is nothing 
    # stopping you calling them directly
    @staticmethod
    def _generate_staff_id():
        # access class variables using the class name
        next_staff_id = Staff.next_staff_id
        Staff.next_staff_id += 1
        return next_staff_id

    # overriding properties example
    # say we want to raise the minimum age for staff
    @Person.age.setter
    def age(self, value):
        if value < 35 or value > 80:
            raise ValueError("Invalid age for a staff member!")

        self._age = value


# making objects:
me = Person("Peter", "O'Connor", 38)
print(type(me))

# check its instance variables via the properties
print(me.first_name)
print(me.surname)
print(me.age)

# calling methods
me.to_string()

# creating an inherited class - Staff member
doc = Staff("Emmett", "Brown", 62)
# __dict__ magic method is useful to print out a dict representation of an object
print(doc.__dict__)
