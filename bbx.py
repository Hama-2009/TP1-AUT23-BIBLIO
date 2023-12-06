import datetime
import csv

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age


class Adherent(Personne):
    def __init__(self, p, numAdherent):
        super().__init__(p.nom, p.prenom, p.age)
        self.numAdherent = numAdherent

    def __eq__(self, other):
        return self.numAdherent == other.numAdherent

class Document:
    def __init__(self, titre, nombrePages, ISBN):
        self.titre = titre
        self.nombrePages = nombrePages
        self.ISBN = ISBN
class Livre(Document):
    def __init__(self, doc, auteur, maisonEdition, emprunte=False):
        super().__init__(doc.titre, doc.nombrePages, doc.ISBN)
        self.emprunte = emprunte
        self.auteur = auteur
        self.maisonEdition = maisonEdition
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
        emprunt.date_retour = datetime.datetime.now().strftime("%Y-%m-%d")

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
                adherent = Adherent(Personne(nom, prenom, age), numAdherent)
                self.bibliotheque.ajouter_adherent(adherent)

            elif choix == '2':
                numAdherent = input("Entrez le ID de l'adhérent à supprimer : ")
                adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                if adherent:
                    self.bibliotheque.supprimer_adherent(adherent)
                else:
                    print("Adhérent non trouvé.")
            elif choix == '3':
                for adherent in self.bibliotheque.adherents:
                    print(f"{adherent.numAdherent} {adherent.nom} {adherent.prenom} {adherent.age}")
            elif choix == '4':
                titre = input("Entrez le titre du livre : ")
                nombrePages = input("Entrez le nombrePages du livre : ")
                ISBN = input("Entrez le ISBN du livre : ")
                auteur = input (" auteur : ")
                maisonEdition = input ("maison : ")
                livre = Livre(Document(titre, nombrePages, ISBN), auteur, maisonEdition)
                self.bibliotheque.ajouter_livre(livre)
            elif choix == '5':
                titre = input("Entrez le titre du livre à supprimer : ")
                livre = next((l for l in self.bibliotheque.livres if l.titre == titre), None)
                if livre:
                    self.bibliotheque.supprimer_livre(livre)
                else:
                    print("Livre non trouvé.")
            elif choix == '6':
                for livre in self.bibliotheque.livres:
                    print(f" Titre:{livre.titre} ISBN:{livre.ISBN}  est {'pas' if not livre.emprunte else ''} emprunté")
            elif choix == '7':
                numAdherent = input("Entrez le ID de l'adhérent qui emprunte : ")
                adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                if not adherent:
                    print("Adhérent non trouvé.")
                    continue

                titre = input("Entrez le titre du livre emprunté : ")
                livre = next((l for l in self.bibliotheque.livres if l.titre == titre), None)
                if not livre:
                    print("Livre non trouvé.")
                    continue

                date_emprunt = datetime.datetime.now().strftime("%Y-%m-%d")
                emprunt = Emprunt(adherent, livre, date_emprunt)
                self.bibliotheque.ajouter_emprunt(emprunt)
                livre.emprunte = True
            elif choix == '8':
                numAdherent = input("Entrez le ID de l'adhérent qui retourne le livre : ")
                adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                if not adherent:
                    print("Adhérent non trouvé.")
                    continue

                titre = input("Entrez le titre du livre à retourner : ")
                livre = next((l for l in self.bibliotheque.livres if l.titre == titre), None)
                if not livre:
                    print("Livre non trouvé.")
                    continue

                emprunt = next((e for e in self.bibliotheque.emprunts if e.adherent == adherent and e.livre == livre and e.date_retour is None), None)
                if emprunt:
                    self.bibliotheque.retourner_emprunt(emprunt)
                    livre.emprunte = False
                else:
                    print("Emprunt non trouvé.")
            elif choix == '9':
                self.bibliotheque.afficher_emprunts()
            else:
                print("Choix invalide, veuillez réessayer.")


bibliotheque = Bibliotheque()
interface = InterfaceUtilisateur(bibliotheque)
interface.run()


