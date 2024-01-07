import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2


rectangle = Rectangle(largeur=4, hauteur=3)
resultat_aire_rectangle = rectangle.aire()


cercle = Cercle(radius=2)
resultat_aire_cercle = cercle.aire()


print(f"L'aire du rectangle est : {resultat_aire_rectangle}")
print(f"L'aire du cercle est : {resultat_aire_cercle}")
