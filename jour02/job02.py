class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur

    def getNombrePages(self):
        return self.__nombre_pages


    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def setAuteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

livre1 = Livre(titre="Harry Potter", auteur="J.K. Rowling", nombre_pages=400)

print("Titre du livre :", livre1.getTitre())
print("Auteur du livre :", livre1.getAuteur())
print("Nombre de pages du livre :", livre1.getNombrePages())


livre1.setTitre("Le Seigneur des Anneaux")
livre1.setAuteur("J.R.R. Tolkien")
livre1.setNombrePages(600)


print("Nouveau titre du livre :", livre1.getTitre())
print("Nouvel auteur du livre :", livre1.getAuteur())
print("Nouveau nombre de pages du livre :", livre1.getNombrePages())


livre1.setNombrePages(-50)  

