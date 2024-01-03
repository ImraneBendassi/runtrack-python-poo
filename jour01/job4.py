class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."


personne1 = Personne(nom="Doe", prenom="John")
personne2 = Personne(nom="Smith", prenom="Jane")
personne3 = Personne(nom="Dupont", prenom="Pierre")


print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
