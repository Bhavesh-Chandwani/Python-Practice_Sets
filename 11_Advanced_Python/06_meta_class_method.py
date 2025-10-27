class Meta(type):
    @property
    def species(cls):
        return cls._species

    @species.setter
    def species(cls, new_species):
        cls._species = new_species


class Animal(metaclass=Meta):
    _species = "Mammal"


print(Animal.species)
# demonstrate the setter works at class level
Animal.species = "Bird"
print(Animal.species)

'''
A metaclass is “the class of a class.” In Python, classes are objects created from a metaclass. By default the metaclass is type. A metaclass controls how a class is created (its attributes, methods, or behavior) — you can use one to customize class construction, inject attributes, validate class definitions, or provide class-level descriptors/properties.
'''