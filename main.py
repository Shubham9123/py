class Person:def
__init__ (self, name, surname, age):
self.name = name self.surname = surname self.age = age def greetings (self):
print ("Hello", self.name, self.surname + ". Glad you are", self.age,
       "years old.") p1 = Person ("Linus", "Torvalds", 52) p1.greetings ()
