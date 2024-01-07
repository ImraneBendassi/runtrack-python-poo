class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def getNom(self):
        return self.__nom

    def getNombreHabitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.augmenter_population()

    def ajouter_population(self):
        self.__ville.augmenter_population()


paris = Ville(nom="Paris", nombre_habitants=1000000)
marseille = Ville(nom="Marseille", nombre_habitants=861635)


print(f"Nombre d'habitants à {paris.getNom()} : {paris.getNombreHabitants()}")
print(f"Nombre d'habitants à {marseille.getNom()} : {marseille.getNombreHabitants()}")


john = Personne(nom="John", age=45, ville=paris)
myrtille = Personne(nom="Myrtille", age=4, ville=paris)
chloe = Personne(nom="Chloé", age=18, ville=marseille)


print(f"Nombre d'habitants à {paris.getNom()} après l'arrivée de nouvelles personnes : {paris.getNombreHabitants()}")
print(f"Nombre d'habitants à {marseille.getNom()} après l'arrivée de nouvelles personnes : {marseille.getNombreHabitants()}")
