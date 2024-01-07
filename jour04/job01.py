
class Personne:
    def __init__(self, age=14):
        self.age = age

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def bonjour(self):
        print("Salut, je suis l'élève!")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print(f"Le cours de {self.matiereEnseignee} va commencer")


eleve = Eleve(age=15)
eleve.bonjour()
eleve.allerEnCours()


professeur = Professeur(age=40, matiereEnseignee="Mathématiques")
professeur.bonjour()
professeur.enseigner()

