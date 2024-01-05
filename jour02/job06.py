class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "En cours"

    
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Erreur : Le plat '{nom_plat}' est déjà dans la commande.")

    
    def annuler_commande(self):
        self.__statut_commande = "Annulée"
        print("La commande a été annulée.")


    def afficher_commande(self):
        print(f"\nCommande #{self.__numero_commande} - Statut : {self.__statut_commande}")
        print("Plats commandés:")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"  - {nom_plat} : {plat['prix']} € - Statut : {plat['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer : {total} €")


    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva


commande1 = Commande(numero_commande=1)


commande1.ajouter_plat("Pizza Margherita", 10.0)
commande1.ajouter_plat("Salade César", 8.0)
commande1.ajouter_plat("Spaghetti Bolognaise", 12.0)


commande1.afficher_commande()


tva = commande1.calculer_tva(taux_tva=10)
print(f"Montant de la TVA : {tva} €")


commande1.annuler_commande()


commande1.afficher_commande()
