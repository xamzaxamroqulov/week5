# Classes - Chapter 9
# Class - general template, where you have description and behaviour anything you wanted to represent
# class name always starts with capital letter

class Dog():
    """This is the general class about Dog."""
    # Attribute(properties)
    breed = ''
    name = ''

    # Behaviour, methods
    def bark(self):
        print("wouf wouf!!")


class NewDog():
    """This is the New class about Dog with mandatory parameters."""

    def __init__(self, name, age):  # initiation/ constructor
        self.name = name
        self.age = age
        print("constructing the New Dog class.")

    # Behaviour, methods
    def bark(self):
        """barking method"""
        print(f"{self.name} is barking : wouf wouf!!")

    def get_name(self):
        """getting the name"""
        print(self.name)

# Object is the instance(representation in specific way) of class
dog1 = Dog()  # mydog is the object of Dog() class, this process is called intantiation
dog1.breed = 'German shepard'
dog1.name = 'Rex'
# dog1.bark()

dog2 = Dog()
dog2.name = "Bobik"
dog2.breed = 'pudo'
# dog2.bark()

print('Name of dog1', dog1.name)
print('Breed of dog1', dog1.breed)
dog1.bark()

print('Name of dog2', dog2.name)
print('breed of dog2', dog2.breed)
dog2.bark()

print("--------------")
dog3 = NewDog('Sharik', 4)
dog3.bark()
dog3.get_name()

dog4 = NewDog(age=3, name='Hatika')
dog4.bark()
dog4.get_name()
# dog4.age

help(NewDog)