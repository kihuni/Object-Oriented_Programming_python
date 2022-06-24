
class Person:
    countPerson = 0
    
    def __init__(self, name):
        self.name = name

        print("initializing {}".format(self.name))

        Person.countPerson +=1
    
    def removePerson(self):
        print("{} Was removed from person category!".format(self.name))

        Person.countPerson -=1

        if Person.countPerson == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("there are still {:d} left".format(Person.count))
        
newPerson = Person("kamau")
newPerson.removePerson()

# initializing kamau
# kamau Was removed from person category!
# kamau was the last one.

    

