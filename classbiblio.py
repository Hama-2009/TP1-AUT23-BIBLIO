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