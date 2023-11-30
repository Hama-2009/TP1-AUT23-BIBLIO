<<<<<<< Updated upstream
class Document:
    def __init__(self, titre, nombrePages, ISBN):
        self.titre = titre
        self.nombrePages = nombrePages
        self.ISBN = ISBN
    def __str__(self):
        return "[Document : " + self.titre + "]"

    @classmethod
    def lireDepuisClavier(self):
        titre = input("Document.titre = ")
        nombrePages = input("Document.nombrePages = ")
        ISBN = input("Document.ISBN = ")
        return Document(titre, nombrePages, ISBN)


class Livre(Document):
    def __init__(self, doc, auteur, maisonEdition):
        super().__init__(doc.titre, doc.nombrePages, doc.ISBN)
        self.auteur = auteur
        self.maisonEdition = maisonEdition
    def __str__(self):
        return "[Livre : " + self.titre + "]"
class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def __str__(self):# mÃ©thode qui retourn un string qui decrit l'objet
        return "[" + self.nom + " " + self.prenom + " " + str(self.age) + "]"
class Adherent(Personne):
    def __init__(self, personne, numAdherent):
        super().__init__(personne.prenom, personne.nom, personne.age)
        self.numAdherent = numAdherent
    def __str__(self):# mÃ©thode qui retourn un string qui decrit l'objet
        return "[" + self.nom + " " + str(self.numAdherent) + "]"
class Emprunt:
    def __init__(self, adherent, document, dateEmprunt):
        self.adherent = adherent
        self.document = document
        self.dateEmprunt = dateEmprunt
    def __str__(self):# mÃ©thode qui retourn un string qui decrit l'objet
        return "[" + str(self.adherent) + " " + self.document.__str__() + "]" + " [Retour" + self.dateEmprunt + " ]"
class Biblio:
    def __init__(self):
        self.listeDocument = []
        self.listeAdherent = []
        self.listeEmprunts = []

    def ajouterEmprunt(self, emprunt):
        self.listeEmprunts.append(emprunt)
    def afficherListeEmprunt(self):
        for x in self.listeEmprunts:
            print(x)

    def ajouterDocument(self, doc):
        self.listeDocument.append(doc)
    def supprimerDocument(self, doc):
        self.listeDocument.remove(doc)
    def afficherListeDocument(self):
        for x in self.listeDocument:
            print(x)
    def getDocumentByIndex(self,index):
        return self.listeDocument[index]

    def ajouterAdherent(self, ad):
        self.listeAdherent.append(ad)
    def supprimerAdherent(self, ad):
        self.listeAdherent.remove(ad)
    def afficherListeAdherent(self):
        for x in self.listeAdherent:
            print(x)
    def getAdherentByIndex(self,index):
        return self.listeAdherent[index]

maBiblio = Biblio()
maBiblio.ajouterDocument(Document("document1", 45, 4564789))
#polymorphisme : Lorsque le livre est un document
maBiblio.ajouterDocument(Livre(Document("Miserable", 800, 456789), "Hugo ", "maison Edition Montreal "))

maBiblio.ajouterAdherent(Adherent(Personne("Cancino", "Pablo", 28), 12345))


maBiblio.ajouterEmprunt(Emprunt( maBiblio.getAdherentByIndex(0),maBiblio.getDocumentByIndex(0), "2023-03-30"))
maBiblio.ajouterEmprunt(Emprunt( maBiblio.getAdherentByIndex(0),maBiblio.getDocumentByIndex(1), "2023-03-30"))


d1 = Document.lireDepuisClavier()
maBiblio.ajouterDocument(d1)

# Hopital = liste clients, liste medecin, liste rdv, liste locaux

maBiblio.afficherListeDocument()
maBiblio.afficherListeAdherent()
maBiblio.afficherListeEmprunt()
=======
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
    def __init__(self, titre, nombrePages, ISBN, emprunte=False):
        self.titre = titre
        self.nombrePages = nombrePages
        self.ISBN = ISBN
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
                adherent = Adherent(nom, prenom, age, numAdherent)
                self.bibliotheque.ajouter_adherent(adherent)
            elif choix == '2':
                nom = input("Entrez le nom de l'adhérent à supprimer : ")
                prenom = input("Entrez le prénom de l'adhérent à supprimer : ")
                age = input("Entrez l'age de l'adhérent à supprimer : ")
                numAdherent = input("Entrez le ID de l'adhérent à supprimer : ")
                adherent = Adherent(nom, prenom, age, numAdherent)
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
                date_emprunt = datetime.datetime.now().strftime("%Y-%m-%d")
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
>>>>>>> Stashed changes
