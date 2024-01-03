class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)


joueur = Personnage(x=3, y=4)


print("Position initiale du joueur :", joueur.position())


joueur.gauche()


print("Nouvelle position du joueur après avoir bougé à gauche :", joueur.position())


joueur.haut()


print("Nouvelle position du joueur après avoir bougé vers le haut :", joueur.position())
