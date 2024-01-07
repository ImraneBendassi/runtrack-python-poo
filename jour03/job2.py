class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde_initial, autorisation_decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert_autorise = autorisation_decouvert

    def afficher(self):
        print(f"Compte {self.__numero_compte} - {self.__nom} {self.__prenom}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert_autorise:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Erreur : Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * (taux_agios / 100)
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert_autorise:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Erreur : Solde insuffisant pour effectuer le virement.")


compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde_initial=1000)


compte1.afficher()


compte1.afficherSolde()


compte1.versement(500)


compte1.retrait(200)


compte1.agios(taux_agios=2)


compte2 = CompteBancaire(numero_compte="654321", nom="Durand", prenom="Marie", solde_initial=-500, autorisation_decouvert=True)


compte1.virement(compte_destinataire=compte2, montant=300)


compte1.afficherSolde()
compte2.afficherSolde()
