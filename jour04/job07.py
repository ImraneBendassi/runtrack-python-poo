import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def valeur_carte(self, carte):
        if carte.valeur in ['J', 'Q', 'K']:
            return 10
        elif carte.valeur == 'A':
            return 11
        else:
            return int(carte.valeur)

    def jouer_partie(self):
        joueur = self.tirer_carte(), self.tirer_carte()
        croupier = self.tirer_carte(), self.tirer_carte()

        print(f"Main du joueur : {self.main_en_texte(joueur)}")
        print(f"Main du croupier : {self.main_en_texte([croupier[0]])}")

        while input("Voulez-vous tirer une carte ? (o/n): ").lower() == 'o':
            joueur += self.tirer_carte(),

            if self.calculer_points(joueur) > 21:
                print("Vous avez dépassé 21 points. Vous avez perdu.")
                return

            print(f"Main du joueur : {self.main_en_texte(joueur)}")

        while self.calculer_points(croupier) < 17:
            croupier += self.tirer_carte(),

        print(f"Main du croupier : {self.main_en_texte(croupier)}")

        if self.calculer_points(joueur) > 21:
            print("Vous avez dépassé 21 points. Vous avez perdu.")
        elif self.calculer_points(joueur) > self.calculer_points(croupier):
            print("Vous avez gagné !")
        elif self.calculer_points(joueur) < self.calculer_points(croupier):
            print("Le croupier a gagné.")
        else:
            print("Égalité !")

    def tirer_carte(self):
        return self.paquet.pop()

    def main_en_texte(self, main):
        return ', '.join([f"{carte.valeur} de {carte.couleur}" for carte in main])

    def calculer_points(self, main):
        points = sum(self.valeur_carte(carte) for carte in main)

        
        for carte in main:
            if carte.valeur == 'A' and points > 21:
                points -= 10

        return points


jeu = Jeu()
jeu.jouer_partie()
