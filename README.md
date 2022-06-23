# The self 

- unlike functions in python, Class methods they must have a variable added to the beggining of the parameter list
- Note You donot need to give a value for the parameter when calling the method.
- Python provide it automatically.
- By convention the name given to the variable is self

# How does python gives a value for self

- say you have a class called myclass and an instance of this class called myobject.
- When you call a method of this object as myobject.method(arg1, arg2) this is automatically converted by python into myclass.method(myobject, arg1,arg2) this is all the special self is about

