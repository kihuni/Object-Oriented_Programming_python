# Inheritance

- Inheritance enables us to create a class and inherit its methods and properties(fields) to others classes
- Inshort inheritance is implementing a type and and subtype relationship

- Inheritance enables us to reuse our code. For example:

- supposed you have two types; teachers and students in a school.lets say they have some commom characteristics such as name, age and address and also they have specific characteristics  of their own such as salary, courses and leaves of teachers and, marks and fees for students.

- Instead of creating two independent classes for each type and process them but when adding a new common characteristic would mean adding to both of these independent classes

- But implementing inheritance, you can create base classes `SchoolMember` and then have the two classes(`derived classes or subclasses`), the teacher and the student classes `inherit` from this class. `i.e`They became sub-types of this base class and then we can add specific characteristics to these sub-types

- As a result if you add or change any functionality in base class is automatically reflected in the subtypes as well.

- Another Advantage of inheritance is that you can refer to a `sub-class`(`teacher and student`) object as a (`SchoolMember`) `base-class` 

- The process where a `sub-type(teachers and student)` can be subtituted in any situation where a parent type(`SchoolMember`)is expected is what we call `polymorphism`: object can be treated as an instance of the parent class.

## lets walk through the example given [here](https://github.com/kihuni/Object-Oriented_Programming_python/blob/main/inheritance/Inheritance.py)

- 

