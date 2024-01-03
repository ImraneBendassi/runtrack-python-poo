class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom


animal_instance = Animal()


print("Âge de l'animal :", animal_instance.age)
animal_instance.vieillir()


print("Âge de l'animal après vieillissement :", animal_instance.age)


animal_instance.nommer("Ludo")


print("Nom de l'animal :", animal_instance.prenom)
