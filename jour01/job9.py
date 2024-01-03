class Produit:
    def __init__(self, nom, prixHT, tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        return f"Informations sur le produit - Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.tva}%"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.tva


produit1 = Produit(nom="Livre", prixHT=20.0, tva=5.5)
produit2 = Produit(nom="Ordinateur", prixHT=800.0, tva=20.0)
produit3 = Produit(nom="Téléphone", prixHT=300.0, tva=10.0)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())


print("Prix TTC du produit 1 :", produit1.calculerPrixTTC())
print("Prix TTC du produit 2 :", produit2.calculerPrixTTC())
print("Prix TTC du produit 3 :", produit3.calculerPrixTTC())


produit1.modifierNom("Roman")
produit1.modifierPrixHT(15.0)

produit2.modifierNom("Laptop")
produit2.modifierPrixHT(750.0)

produit3.modifierNom("Smartphone")
produit3.modifierPrixHT(280.0)


print("Nouveau prix du produit 1 :", produit1.calculerPrixTTC())
print("Nouveau prix du produit 2 :", produit2.calculerPrixTTC())
print("Nouveau prix du produit 3 :", produit3.calculerPrixTTC())
