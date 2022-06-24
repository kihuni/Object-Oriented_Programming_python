class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print('Hi, I am', self.name)

p = Person('Stephen') #initialize object
p.say_hi() # 'Hi, I am Stephen'