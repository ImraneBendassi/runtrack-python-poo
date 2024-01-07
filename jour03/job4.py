class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"\nStatistiques de {self.nom} (Joueur #{self.numero}):")
        print(f"Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"Joueur {joueur.nom} ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero_joueur, action):
        for joueur in self.joueurs:
            if joueur.numero == numero_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe_decisive":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action non reconnue.")


joueur1 = Joueur(nom="Messi", numero=10, position="Attaquant")
joueur2 = Joueur(nom="Ronaldo", numero=7, position="Attaquant")
joueur3 = Joueur(nom="Neymar", numero=11, position="Milieu")


equipe1 = Equipe(nom="Barcelone")
equipe2 = Equipe(nom="Real Madrid")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


equipe1.mettreAJourStatistiquesJoueur(numero_joueur=10, action="but")
equipe1.mettreAJourStatistiquesJoueur(numero_joueur=11, action="passe_decisive")
equipe2.mettreAJourStatistiquesJoueur(numero_joueur=7, action="carton_jaune")


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
