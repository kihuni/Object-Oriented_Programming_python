## Class And Object Variables

- When dealing with data we need to keep in mind the context in where their storage are defined.There are two types of fields(variables):
    - Class variables and object variables: they are classified depending on whether the class or the objects owns the variable.

## Class variables

- When we talk about class variables we mean that they can be accessed by all instances of that class.

  `N/B` When you make any changes on the variable, the change is seen by all the other instances
    
# Object Variables

- This is available or accessible only on the individual instance `i.e` its owned by each instance/object

 ### A walk through the example given [here](https://github.com/kihuni/Object-Oriented_Programming_python/blob/main/classVariables_objectVariables/class-objects_variable.py)

Before that note that:
    - The variable class belongs to the `Person class`: its a class variable

    - The `name` variable belongs to the object: its an object variable
- In the __init__ method we initialize the `Person` instance with a `name` and inside the method we are incrementing `countPerson` by 1 to keep record of person added

- In the remove method, we are also decrementing `countPerson` by 1 to keep record of number of person removed
- We are also implementing condition to keep record on nmber of people left