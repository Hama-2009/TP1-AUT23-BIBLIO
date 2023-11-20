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
