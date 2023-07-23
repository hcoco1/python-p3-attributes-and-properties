#!/usr/bin/env python3



APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and (1<=len(name)<=25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed 
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
    
    
#The code first defines a list of approved dog breeds called APPROVED_BREEDS. The list contains 8 dog breeds.

#The code then defines a class called Dog. The Dog class has two properties: name and breed. The name property is a string that represents the dog's name. The breed property is a string that represents the dog's breed.

#The name property has two methods: get_name() and set_name(). The get_name() method simply returns the value of the _name attribute. The set_name() method takes a name argument and sets the value of the _name attribute to the value of the argument. The set_name() method also validates the value of the name argument, ensuring that it is a string between 1 and 25 characters long.

#The breed property has two methods: get_breed() and set_breed(). The get_breed() method simply returns the value of the _breed attribute. The set_breed() method takes a breed argument and sets the value of the _breed attribute to the value of the argument. The set_breed() method also validates the value of the breed argument, ensuring that it is one of the approved breeds in the APPROVED_BREEDS list.

#The code then creates a new Dog object and sets the name property to "fido" and the breed property to "Mastiff". The code then prints the value of the name property and the breed property.     
     