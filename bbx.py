import datetime

class Adherent:
    def __init__(self, nom, prenom, age, numAdherent):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.numAdherent = numAdherent
    def __eq__(self, other):
        return self.numAdherent == other.numAdherent
class Livre:
    def __init__(self, titre, emprunte=False):
        self.titre = titre
        self.emprunte = emprunte

class Emprunt:
    def __init__(self, adherent, livre, date_emprunt, date_retour=None):
        self.adherent = adherent
        self.livre = livre
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour

class Bibliotheque:
    def __init__(self):
        self.adherents = []
        self.livres = []
        self.emprunts = []

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)

    def supprimer_adherent(self, adherent):
        self.adherents.remove(adherent)

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres.remove(livre)

    def ajouter_emprunt(self, emprunt):
        self.emprunts.append(emprunt)

    def retourner_emprunt(self, emprunt):
        emprunt.date_retour = datetime.now().strftime("%Y-%m-%d")

    def afficher_emprunts(self):
        for emprunt in self.emprunts:
            print(f"{emprunt.adherent.nom} {emprunt.adherent.prenom} a emprunté {emprunt.livre.titre} le {emprunt.date_emprunt}")

class InterfaceUtilisateur:
    def __init__(self, bibliotheque):
        self.bibliotheque = bibliotheque

    def menu(self):
        print("""
        1       Ajouter adhérent
        2       Supprimer adhérent
        3       Afficher tous les adhérents
        4       Ajouter Livre
        5       Supprimer Livre
        6       Afficher tous les Livres
        7       Ajouter Emprunt
        8       Retour d’un Emprunt
        9       Afficher tous les Emprunts
        Q      Quitter
        """)

    def run(self):
        while True:
            self.menu()
            choix = input("Choisissez une action : ")

            if choix == 'Q':
                break
            elif choix == '1':
                nom = input("Entrez le nom de l'adhérent : ")
                prenom = input("Entrez le prénom de l'adhérent : ")
                age = input("Entrez l'age de l'adhérent : ")
                numAdherent = input("Entrez le ID de l'adhérent : ")
                adherent = Adherent(nom, prenom, age,numAdherent)
                self.bibliotheque.ajouter_adherent(adherent)
            elif choix == '2':
                '''nom = input("Entrez le nom de l'adhérent à supprimer : ")
                prenom = input("Entrez le prénom de l'adhérent à supprimer : ")
                age = input("Entrez l'age de l'adhérent à supprimer : ")'''
                numAdherent = input("Entrez le ID de l'adhérent à supprimer : ")
                adherent = Adherent(numAdherent)
                self.bibliotheque.supprimer_adherent(adherent)
            elif choix == '3':
                for adherent in self.bibliotheque.adherents:
                    print(f"{adherent.numAdherent} {adherent.nom} {adherent.prenom} {adherent.age}")
            elif choix == '4':
                titre = input("Entrez le titre du livre : ")
                livre = Livre(titre)
                self.bibliotheque.ajouter_livre(livre)
            elif choix == '5':
                titre = input("Entrez le titre du livre à supprimer : ")
                livre = Livre(titre)
                self.bibliotheque.supprimer_livre(livre)
            elif choix == '6':
                for livre in self.bibliotheque.livres:
                    print(f"{livre.titre} est {'pas' if not livre.emprunte else ''} emprunté")
            elif choix == '7':
                nom = input("Entrez le nom de l'adhérent qui emprunte : ")
                prenom = input("Entrez le prénom de l'adhérent qui emprunte : ")
                adherent = Adherent(nom, prenom)
                titre = input("Entrez le titre du livre emprunté : ")
                livre = Livre(titre)
                date_emprunt = datetime.now().strftime("%Y-%m-%d")
                emprunt = Emprunt(adherent, livre, date_emprunt)
                self.bibliotheque.ajouter_emprunt(emprunt)
                self.bibliotheque.livres[self.bibliotheque.livres.index(livre)].emprunte = True
            elif choix == '8':
                nom = input("Entrez le nom de l'adhérent qui retourne le livre : ")
                prenom = input("Entrez le prénom de l'adhérent qui retourne le livre : ")
                adherent = Adherent(nom, prenom)
                titre = input("Entrez le titre du livre à retourner : ")
                livre = Livre(titre)
                emprunt = Emprunt(adherent, livre, "inconnue")
                self.bibliotheque.retourner_emprunt(emprunt)
                self.bibliotheque.livres[self.bibliotheque.livres.index(livre)].emprunte = False
            elif choix == '9':
                self.bibliotheque.afficher_emprunts()
            else:
                print("Choix invalide, veuillez réessayer.")

bibliotheque = Bibliotheque()
interface = InterfaceUtilisateur(bibliotheque)
interface.run()