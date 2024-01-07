class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

rectangle = Rectangle(largeur=4, hauteur=3)

resultat_aire = rectangle.aire()

print(f"L'aire du rectangle est : {resultat_aire}")
