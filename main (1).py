class Person:
    def __init__ (self, name, surname, age):
        self.name = name 
        self.surname = surname 
        self.age = age 
    def greetings (self):
        print ("Hello", self.name, self.surname + ". Glad you are", self.age,"years old.")

name = input("Enter your name: ")
surname = input("Enter your surname, {}: ".format(name))
age = input("Please enter your age: ")
p1 = Person (name,surname,age) 
p1.greetings ()
