class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    
    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


rectangle1 = Rectangle(longueur=10, largeur=5)


print("Longueur initiale du rectangle :", rectangle1.getLongueur())
print("Largeur initiale du rectangle :", rectangle1.getLargeur())


rectangle1.setLongueur(15)
rectangle1.setLargeur(7)


print("Nouvelle longueur du rectangle :", rectangle1.getLongueur())
print("Nouvelle largeur du rectangle :", rectangle1.getLargeur())
