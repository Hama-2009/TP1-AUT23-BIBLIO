import json

class Adherent:
    def __init__(self, nom, prenom, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant

class Bibliotheque:
    def __init__(self):
        self.adherents = []

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)

    def enregistrer_adherents(self, nom_fichier):
        with open(nom_fichier, 'w') as fichier:
            json.dump([adherent.__dict__ for adherent in self.adherents], fichier)

    def charger_adherents(self, nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            data = json.load(fichier)
            self.adherents = [Adherent(**d) for d in data]

class InterfaceUtilisateur:
    def __init__(self, bibliotheque):
        self.bibliotheque = bibliotheque
        self.bibliotheque.charger_adherents('adherents.json')

    def afficher_adherents(self):
        for adherent in self.bibliotheque.adherents:
            print(f"Nom: {adherent.nom}, Prénom: {adherent.prenom}, Identifiant: {adherent.identifiant}")

    def ajouter_adherent(self):
        nom = input("Entrez le nom de l'adhérent: ")
        prenom = input("Entrez le prénom de l'adhérent: ")
        identifiant = input("Entrez l'identifiant de l'adhérent: ")
        adherent = Adherent(nom, prenom, identifiant)
        self.bibliotheque.ajouter_adherent(adherent)
        print("Adhérent ajouté avec succès.")

    def run(self):
        while True:
            print("\n--- Menu ---")
            print("1. Afficher les adhérents")
            print("2. Ajouter un adhérent")
            print("3. Quitter")

            choix = input("Entrez le numéro de votre choix: ")

            if choix == "1":
                self.afficher_adherents()
            elif choix == "2":
                self.ajouter_adherent()
            elif choix == "3":
                break
            else:
                print("Choix non valide, veuillez réessayer.")

    def on_exit(self):
        self.bibliotheque.enregistrer_adherents('adherents.json')

bibliotheque = Bibliotheque()
interface = InterfaceUtilisateur(bibliotheque)
interface.run()
interface.on_exit()