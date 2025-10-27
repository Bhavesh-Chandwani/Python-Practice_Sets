class Animal:
    species = "Mammal"

    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

print(Animal.get_species())
Animal.set_species("Reptile")
print(Animal.get_species())