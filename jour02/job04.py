class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

   
    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getNumeroEtudiant(self):
        return self.__numero_etudiant

    def getCredits(self):
        return self.__credits

    def getLevel(self):
        return self.__level

  
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            print(f"{credits} crédits ajoutés avec succès.")
            self.__level = self.__studentEval()  
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")


    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"


    def studentInfo(self):
        print(f"Informations de l'étudiant {self.__prenom} {self.__nom} ({self.__numero_etudiant}):")
        print(f"  - Niveau: {self.__level}")
        print(f"  - Crédits: {self.__credits}")

john_doe = Student(nom="Doe", prenom="John", numero_etudiant=145)


john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)


john_doe.studentInfo()





