# Object Oriented Programming

- OOP  is a method of structuring a program by bundling related properties and behaviors into individual objects
- It combines data and functionality and wrap it inside an object

- Classes and object are the main building blocks of the OOP.
    - A `class` creates a new `type` where `objects` are `instances` of the `class`
- For Example:
    You can have variables of `type Person`(variables that store attributes of `person`)are variable which are `instances` of `Person class`

# Field and Methods

- Objects can contain fields(variables) that store data and also objects also have functionality which are called methods.

### example

```
class Person:
    def __init__(self, name):
        self.name = name
    def callMe(self):
        print('please call my name: ', self.name)

newPerson = Person('kihuni')
print(newPerson)

```
  In the above example:
  
    a class is created using keyword `class` then followed by the name `class Person`
    
    Inside class block we define two methods:
    
        The 1st method has a property or field of `name`(The name inside the parameter is different from the name(field) inside the block of the `__init__` method)
        
        The 2nd method is `callMe` method as show above

- Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.

- Fields are of two types - they can belong to each `instance/object` of the `class` or they can belong to the `class` itself. They are called `instance variables` and `class variables` respectively.

