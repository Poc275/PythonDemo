# VARIABLES
a = 10
b = 20

c = 10.523
d = True
e = False
f = "Hello, World!"
g = None

# OPERATORS
print(a + b)
print(b - a)

# OPERATORS (+ - * / %)
amount = 14.99
tax = .17
total = amount + amount * tax
print(total)

# INC/DEC
x = 5
x = x + 1
print(x)
x += 1
print(x)
x -= 2
print(x)

# INPUT/STRING FORMATTING
age = int(input("How old are you?"))
decades = age / 10
print("You are " + str(decades) + " decades old")

# CONDITIONALS (< > <= >= == !=)
temperature = 90

if temperature > 80:
    print("It's too hot, stay inside")
elif temperature < 60:
    print("It's too cold, stay inside")
else:
    print("Go outside")

# we can combine using logical operators AND/OR/NOT
# an example of readability in Python
if temperature > 80 or temperature < 60:
    print("Stay inside")
else:
    print("Go outside")

# AND
forecast = "rain"
if temperature > 80 and not forecast == "rain":
    print("Go outside")
else:
    print("Stay inside")


# LISTS & LOOPS
acronyms = []
acronyms.append("BRB")
acronyms.append("TBH")
acronyms.append("LOL")
acronyms.append("IMHO")
acronyms.append("IDK")
print(acronyms)
print(acronyms[0])

acronyms.remove("TBH")
print(acronyms)

acronym = "TBH"
if acronym in acronyms:
    print(acronym + " is in the list")
else:
    print(acronym + " is NOT in the list")

for acronym in acronyms:
    print(acronym)

# LIST COMPREHENSION
tlas = [acronym.lower() for acronym in acronyms if len(acronym) == 3]
print(tlas)

# LIST METHODS sum/len
lunch_expenses = [10.5, 8, 5, 15, 20, 5, 3]
lunch_total = 0

len(acronyms)

for x in lunch_expenses:
    lunch_total = lunch_total + x

print("You spent £", lunch_total)
print("You spent £{0:2f}".format(sum(lunch_expenses)))

# FOR LOOPS USING range()
for i in range(7):
    print(i)

# NESTED LISTS
breakfast_menu = ["English", "Continental"]
lunch_menu = ["BLT", "Chicken Salad", "Soup"]
dinner_menu = ["Spaghetti", "Steak", "Salad", "Carvery"]
menus = [breakfast_menu, lunch_menu, dinner_menu]

# use 2 indexes to get an element
print(menus[0][1])


# DICTIONARIES
# key/value store
# keys/values can be of any type, even lists/other dictionaries
acronyms_dict = {
    "LOL": "Laugh out loud",
    "IDK": "I don't know",
    "TBH": "To be honest",
}
print(acronyms_dict)
print(acronyms_dict["TBH"])

# update value
acronyms_dict["IDK"] = "blah"

# remove
del acronyms_dict["LOL"]

print(acronyms_dict)

# check a key exists
definition = acronyms_dict.get("BRB")
print(definition)

# looping requires two variables, key/value
# retrieved via the items() method
for k, v in acronyms_dict.items():
    print(k, ": ", v)

# we can use dictionaries to represent complex objects
me = {
    "name": "Peter",
    "city": "Derby",
    "age": 38,
    "favourite_foods": [
        "Pasta",
        "Curry",
        "Sushi"
    ],
    "contact": {
        "home": "me@home.co.uk",
        "work": "me@work.com"
    }
}
print(me)
