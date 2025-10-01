# Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.
# OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOPs, object has attributes thing that has specific data and can perform certain actions using methods.

# OOPs Concepts in Python
# Class in Python
# Objects in Python
# Polymorphism in Python
# Encapsulation in Python
# Inheritance in Python
# Data Abstraction in Python

# Python Class :A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

# Python Objects : An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.
# An object consists of:
# State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

# __init__ Method : __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

# Class Variables : These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Variables : Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

class Dog:
    species = "Canine"
    
    def __init__(self, name , age):
        self.name = name 
        self.age = age

dog1 = Dog("Buddy",3)
dog2 = Dog("Charlie ",5)
print(dog1.species)
print(dog1.name)
print(dog2.name)

dog1.name = "max"
print(dog1.name)

Dog.species = "Feline"
print(Dog.species)
print(dog2.species)