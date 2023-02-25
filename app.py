# Bonus Topic Object Oriented Programming

# A Constructor is something you call to create an instance of an object, this is the special function that Python knows to look for
# specifically named __init__() (two underscores in python is special functions)

# Self is the same as THIS in javascript, a reference to the instance of the object itself (the self will point to the specific var or obj that is 'John' or 'Jane' eg.)
# You can put as many args after SELF as needed

# Define a Class (in pascal case, every new word is Capitalized see 'Employee', eg. format'ClassName')

# THE NONE PART CAN BE ADDED OR LEFT OUT MARK SAID
# class Employee:
#     def __init__(self) -> None:

# This is just us defining a structure, like PROPS in Vue Components, something gets passed whenever a component is created
# Similarly something gets passed to Employee Obj when its created.
# HINT: If you don't want any args just keep it as __init__(self)
# class Employee:
#     def __init__(self, f_name, l_name):
#         self.first_name = f_name
#         self.last_name = l_name

# Functions will be nested in the class, every class function also needs SELF as the first argument.
# The number of args doesn't have to match the listed variables, see Pay.
# Some args can start as blank, eg Location might not be assigned to employee yet so it's None.
# class Employee:
#     def __init__(self, f_name, l_name):
#         self.first_name = f_name
#         self.last_name = l_name
#         # each employee will always default to 15 if this is left as-is
#         self.pay = 15
#         self.location = None

#     def say_name(self):
#         print(self.first_name, self.last_name)

# Inheritance is the most common OOP, parents pass down traits to their children
# a child object will inherit the functionality of the parent class
# class ValueTooSmall(Exception):
#     def __init__(self):
#         # super() refers to the init of the exception class
#         super().__init__("The value is too small.")

# excep1 = Exception("You hit an exception.")
# print(excep1)
# exep2 = ValueTooSmall()
# print(exep2)

# value = int(input("Please enter a number:"))
# if (value < 10):
#     raise ValueTooSmall()

# Inheritance with Employee Example:
class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
    def say_name(self):
        print(self.first_name, self.last_name)

# self.pay is a function variable
# pay=15, if its not specified then pay defaults to 15
class Employee(Person):
    def __init__(self, f_name, l_name, pay=15):
        super().__init__(f_name, l_name)
        # each employee will always default to 15 if this is left as-is
        self.pay = pay
        self.location = None
    def pay_raise(self, amount):
        self.pay = self.pay + amount 

emp_one = Employee("Siobhan","Eykelbosh")
emp_two = Employee("Craig", "Eykelbosh")
emp_three = Employee("Michelle", "Egan", 20)

# print(emp_one.first_name, emp_one.last_name)
# print(emp_two.first_name, emp_two.last_name)

emp_one.say_name()
emp_two.say_name()
print(emp_one.pay)
emp_one.pay_raise(2)
print(emp_one.pay)
print(emp_three.pay)

