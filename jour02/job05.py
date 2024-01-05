class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Assesseurs (getters)
    def getMarque(self):
        return self.__marque

    def getModele(self):
        return self.__modele

    def getAnnee(self):
        return self.__annee

    def getKilometrage(self):
        return self.__kilometrage

    def getEnMarche(self):
        return self.__en_marche

    def getReservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def setMarque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def setModele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def setAnnee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def setKilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def setEnMarche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Erreur : La voiture ne peut pas démarrer. Le réservoir est trop bas.")


    def arreter(self):
        self.__en_marche = False
        print("La voiture s'est arrêtée.")


    def __verifier_plein(self):
        return self.__reservoir > 5


ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, kilometrage=15000)


print("Marque de la voiture :", ma_voiture.getMarque())
print("Modèle de la voiture :", ma_voiture.getModele())
print("Année de la voiture :", ma_voiture.getAnnee())
print("Kilométrage de la voiture :", ma_voiture.getKilometrage())
print("En marche :", ma_voiture.getEnMarche())
print("Réservoir de la voiture :", ma_voiture.getReservoir())


ma_voiture.demarrer()


print("En marche après démarrage :", ma_voiture.getEnMarche())


ma_voiture.arreter()


print("En marche après arrêt :", ma_voiture.getEnMarche())
