import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 20)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        try:
            self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))
        except ValueError:
            print("Veuillez entrer un nombre.")

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 70
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 90
        else:
            print("Niveau non valide. Le jeu sera lancé au niveau 1.")
            vie_joueur = 100
            vie_ennemi = 50

        joueur = Personnage(nom="Joueur", vie=vie_joueur)
        ennemi = Personnage(nom="Ennemi", vie=vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu ! Vous avez gagné !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! Vous avez perdu.")
                break

            print(f"\nStatut actuel :\n{joueur.nom}: {joueur.vie} points de vie\n{ennemi.nom}: {ennemi.vie} points de vie\n")


jeu = Jeu()


jeu.lancerJeu()
