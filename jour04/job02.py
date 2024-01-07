class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self, value):
        if value > 0:
            self._longueur = value
        else:
            print("La longueur doit être positive.")

    @largeur.setter
    def largeur(self, value):
        if value > 0:
            self._largeur = value
        else:
            print("La largeur doit être positive.")

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        if value > 0:
            self._hauteur = value
        else:
            print("La hauteur doit être positive.")

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


rectangle = Rectangle(longueur=5, largeur=3)
print(f"Perimètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")


rectangle.longueur = 7
rectangle.largeur = 4
print(f"Perimètre du rectangle après modification : {rectangle.perimetre()}")
print(f"Surface du rectangle après modification : {rectangle.surface()}")

parallelepipede = Parallelepipede(longueur=4, largeur=2, hauteur=3)
print(f"Perimètre du parallelepipede : {parallelepipede.perimetre()}")
print(f"Surface du parallelepipede : {parallelepipede.surface()}")
print(f"Volume du parallelepipede : {parallelepipede.volume()}")
