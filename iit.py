# Inheritance
# single Inheritance


# multiple Inheritance
# class walk:
#     def walk(self):
#         print("walking")

# class swim:
#     def swim(self):
#         print("swiming")

# class Duck(walk,swim):
#     pass

# # create object
# duck=Duck()
# duck.walk()
# duck.swim()


# class Grandparent:
#     def property(self):
#         print("I have some ancestral property.")

# class Parent(Grandparent):
#     def house(self):
#         print("I have my own house.")

# class Child(Parent):
#     def car(self):
#         print("I have my own car.")


# c = Child()
# c.property()  # from Grandparent
# c.house()     # from Parent
# c.car()       # from Child

# super
# for calling the parent class methods in the child class,use super()
# class A:
#     def greet(self):
#         print("hello from a")

# class B(A):
#     def greet(self):
#         return super().greet() # calling parent method
#     print("hello from b")

# b=B()
# b.greet()


# Encapsulation- it is the concept of building data(variable) and method (function)
# that operate on that data within a single class,while direct acess to some object component
# self.owner=owner
# self.__balance=balance  double underscore means it is not directly acess
# from outside the class
# class Account:
#     def __init__(self,owner,balance):
#         self.owner=owner #public attribute
#         self.__balance=balance # double underscore use for private

#         def deposit(self,amount):
#             if amount >0:
#               self.__balance +=amount

#         def withdraw(self,amount):
#             if 0< amount <= self.__balance:
#                 self.__balance -=amount

#         def get_balance(self):
#             return self.__balance
        
# # object creation
# acc=Account("sintu",10000)
# print(acc.get_balance())


# polymorphism 
# it is the ability for different object types to respond to the same method or
# function call in way specific to their class
# class Dog:
#     def speak(self):
#         return "woof"

# class Cat:
#     def speak(self):
#         return "meow"

# animals=[Dog(),Cat()]

# for animal in animals:
# print(animal.speak())


