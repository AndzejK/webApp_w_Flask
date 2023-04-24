# OOP - commanly repeated tasks and objects can be defined with OOP to create code that is more usable.
# General syntax
class NameOfClass():

    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2
    
    def some_method(self):
        # perform some aciton
        print(self.param1)

class Sample():
    pass

class Dog():

    # Class Object ATTRIBUTES - they are permanently set 
    species='mamal'

    # this kind of attributes too but we assign them by calling the call Dog
    def __init__(self,breed_,name_,owner_):
        self.breed=breed_
        self.name=name_
        self.owner=owner_

breed_1=Dog(breed_='rottweiler',name_='Roy',owner_='Mikka')
# print(f'The owner is: {breed_1.owner}')
# print(breed_1.breed,breed_1.name)
# print(breed_1.species)

class Circle():

    # Attributes 
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    # Methods 
        # No.1 calc radius of circle
    def area(self):
        return self.radius*self.radius*self.pi # r^2*pi
        # No.2 calc the circumference
    def circumference(self):
        return 2*self.pi*self.radius
    

my_circle=Circle(10)    
print(my_circle.radius)
count_the_circle_area=my_circle.area()
print(count_the_circle_area)
print(my_circle.circumference())