# The __init__ Method
- __init__ method is usually run a soon as the object class is instantiated
- Its usually usefull for any initialization

### A walk through of the example given [here](https://github.com/kihuni/Object-Oriented_Programming_python/blob/main/__init__/__init__.py):

- We are creating a class person and inside the class we define two methods:

  - We define __init__ method which takes two parameters the `name`, and along with the usual `self`
  - we have also created a field called `name` which is different from the local variable `name` (defined as a parameter)
  - The benefit of using __init__ is that you do not have to explicitly call the method(This is the speciall significant of this method)
  - It enable us to pass values to your objects
  - The other method is taking self as parameter and printing a string followed the named passed when instantiating the object p
