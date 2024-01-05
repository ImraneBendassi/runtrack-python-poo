class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    
    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur

    def getNombrePages(self):
        return self.__nombre_pages

    def getDisponible(self):
        return self.__disponible

 
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def setAuteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    
    def verification(self):
        return self.__disponible

    
    def emprunter(self):
        if self.verification():
            print("Emprunt du livre en cours...")
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible pour emprunt.")

    
    def rendre(self):
        print("Vérification de l'emprunt du livre...")
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")


livre1 = Livre(titre="Harry Potter", auteur="J.K. Rowling", nombre_pages=400)


print("Titre du livre :", livre1.getTitre())
print("Auteur du livre :", livre1.getAuteur())
print("Nombre de pages du livre :", livre1.getNombrePages())
print("Disponibilité du livre :", livre1.verification())


livre1.emprunter()


print("Disponibilité du livre après emprunt :", livre1.verification())


livre1.rendre()


livre1.emprunter()


livre1.rendre()


print("Disponibilité du livre après rendu :", livre1.verification())
