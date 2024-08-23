from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover_animal(self):
        ...

class Terrestre (Animal):
    def mover_animal(self):
        print("Sou terrestre e estou andando")
class Aquatico (Animal):
    def mover_animal(self):
        print("Sou aquatico e estou nadando")
class Voador (Animal):
    def mover_animal(self):
        print("Sou Voador e estou voando")

class Gato(Terrestre):
    ...
class Baleia(Aquatico):
    pass
class Bentivi(Voador):
    pass
animal_terrestre = Gato()
animal_aquatico = Baleia()
animal_voador = Bentivi()


def mover_animal(animal: Animal):
    animal.mover_animal()

mover_animal(animal_aquatico)
mover_animal(animal_terrestre)
mover_animal(animal_voador)