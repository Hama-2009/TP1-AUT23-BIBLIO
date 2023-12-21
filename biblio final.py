import datetime
import json


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
    def __init__(self, doc, Auteur, maisonEdition, emprunte=False):
        super().__init__(doc.titre, doc.nombrePages, doc.ISBN)
        self.emprunte = emprunte
        self.Auteur = Auteur
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

    def sauvegarder_livres(self, filename="livres.json"):
        livres_data = []
        for livre in self.livres:
            livre_data = {
                "titre": livre.titre,
                "nombrePages": livre.nombrePages,
                "ISBN": livre.ISBN,
                "Auteur": livre.Auteur,
                "maisonEdition": livre.maisonEdition,
                "emprunte": livre.emprunte
            }
            livres_data.append(livre_data)

        with open(filename, "w") as file:
            json.dump(livres_data, file)

    def sauvegarder_adherents(self, filename="adherents.json"):
        adherents_data = []
        for adherent in self.adherents:
            adherent_data = {
                "nom": adherent.nom,
                "prenom": adherent.prenom,
                "age": adherent.age,
                "numAdherent": adherent.numAdherent
            }
            adherents_data.append(adherent_data)

        with open(filename, "w") as file:
            json.dump(adherents_data, file)

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)
        self.sauvegarder_adherents("adherents.json")

    def supprimer_adherent(self, adherent):
        self.adherents.remove(adherent)
        self.sauvegarder_adherents("adherents.json")

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        self.sauvegarder_livres("my_books.json")

    def supprimer_livre(self, livre):
        self.livres.remove(livre)
        self.sauvegarder_livres("my_books.json")

    def ajouter_emprunt(self, emprunt):
        self.emprunts.append(emprunt)

    def supprimer_emprunt(self, emprunt):
        self.emprunts.remove(emprunt)

    def retourner_emprunt(self, emprunt):
        emprunt.date_retour = datetime.datetime.now().strftime("%Y-%m-%d")
        self.supprimer_adherent(emprunt.adherent)
        if emprunt in self.emprunts:
            self.supprimer_emprunt(emprunt)
        if emprunt.livre not in self.livres:
            self.ajouter_livre(emprunt.livre)

        # Affichage de l'état de la liste des livres après le retour
        print("Liste des livres après le retour :")
        print("{:<30} {:<15} {:<10} {:<15}".format("Titre", "ISBN", "Emprunté", "Date d'emprunt"))
        for livre in self.livres:
            emprunte = 'Non'
            date_emprunt = 'Non emprunté'

            for emprunt in self.emprunts:
                if emprunt.livre == livre:
                    if emprunt.date_retour is None:
                        emprunte = 'Oui'
                        date_emprunt = emprunt.date_emprunt
                    else:
                        emprunte = 'Non'
                        date_emprunt = 'Non emprunté'
                    break

            print("{:<30} {:<15} {:<10} {:<15}".format(livre.titre, livre.ISBN, emprunte, date_emprunt))

    def afficher_emprunts(self):
        emprunts_non_rendus = []
        for emprunt in self.emprunts:
            if emprunt.date_retour is None:
                emprunts_non_rendus.append([
                    f"{emprunt.adherent.nom} {emprunt.adherent.prenom}",
                    emprunt.livre.titre,
                    emprunt.date_emprunt,
                    emprunt.date_retour
                ])

        if emprunts_non_rendus:
            print(tabulate(emprunts_non_rendus, headers=["Adhérent", "Livre", "Date d'emprunt", "Date de retour"],
                           tablefmt="pretty"))
        else:
            print("Aucun emprunt en cours.")


class InterfaceUtilisateur:
    def __init__(self, bibliotheque):
        self.bibliotheque = bibliotheque

    def menu(self):
        print("""
        ========== Bienvenue à votre Bibliothèque ========
        | -------------- Faite un choix -----------------|
        | 1 ======> Ajouter adhérent                     |
        | 2 ======> Supprimer adhérent                   |
        | 3 ======> Afficher tous les adhérents          |
        | 4 ======> Ajouter Livre                        |
        | 5 ======> Supprimer Livre                      |
        | 6 ======> Afficher tous les Livres             |
        | 7 ======> Ajouter Emprunt                      |
        | 8 ======> Retour d’un Emprunt                  |
        | 9 ======> Afficher tous les Emprunts           |
        | Q ======> Quitter                              |
        ==================================================
        """)

    def run(self):
        while True:
            self.menu()
            choix = input("Choisissez une action : ")

            if choix == 'Q':
                break
            elif choix == '1':
                while True:
                    # Ajout d'un adhérent
                    nom = input("Entrez le nom de l'adhérent : ")
                    prenom = input("Entrez le prénom de l'adhérent : ")
                    age = input("Entrez l'age de l'adhérent : ")
                    numAdherent = input("Entrez le ID de l'adhérent : ")

                    # Vérification de l'unicité de l'ID de l'adhérent
                    while any(a.numAdherent == numAdherent for a in self.bibliotheque.adherents):
                        print("Cet ID est déjà utilisé. Veuillez en choisir un autre.")
                        numAdherent = input("Entrez le ID de l'adhérent : ")

                    adherent = Adherent(Personne(nom, prenom, age), numAdherent)
                    self.bibliotheque.ajouter_adherent(adherent)
                    print("Adhérent ajouté avec succès")

                    while True:
                        autre_adherent = input("Voulez-vous ajouter un autre adhérent ? (Oui/Non) : ").lower()
                        if autre_adherent == 'non':
                            break
                        elif autre_adherent != 'oui':
                            print("Veuillez entrer 'Oui' ou 'Non'.")
                            continue
                        break
                    if autre_adherent == 'non':
                        break
            elif choix == '2':
                numAdherent = input("Entrez le ID de l'adhérent à supprimer : ")
                adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                if adherent:
                    self.bibliotheque.supprimer_adherent(adherent)
                else:
                    print("Adhérent non trouvé.")
                    input()
            elif choix == '3':
                print("Liste des adhérents :")
                print("ID   | Nom                | Prénom             | Âge")
                for adherent in self.bibliotheque.adherents:
                    print(f"{adherent.numAdherent.ljust(4)} | {adherent.nom.ljust(18)} | {adherent.prenom.ljust(18)} | {adherent.age}")
                input()
            elif choix == '4':
                while True:
                    # Ajout d'un livre
                    titre = input("Entrez le titre du livre : ")
                    nombrePages = input("Entrez le nombre de pages du livre : ")
                    ISBN = input("Entrez le ISBN du livre : ")

                    # Vérification de l'unicité de l'ISBN du livre
                    while any(l.ISBN == ISBN for l in self.bibliotheque.livres):
                        print("Ce ISBN est déjà utilisé. Veuillez en choisir un autre.")
                        ISBN = input("Entrez le ISBN du livre : ")

                    Auteur = input("Auteur : ")
                    maisonEdition = input("Maison d'édition : ")
                    livre = Livre(Document(titre, nombrePages, ISBN), Auteur, maisonEdition)
                    self.bibliotheque.ajouter_livre(livre)
                    print("Livre ajouté avec succès")

                    while True:
                        autre_livre = input("Voulez-vous ajouter un autre livre ? (Oui/Non) : ").lower()
                        if autre_livre == 'non':
                            break  # Pour revenir au menu principal
                        elif autre_livre != 'oui':
                            print("Veuillez entrer 'Oui' ou 'Non'.")
                            # Re-demander la réponse
                            continue
                        # Ajouter un autre livre
                        break  # Sortir de la boucle pour ajouter un autre livre
                    if autre_livre == 'non':
                        break  # Pour revenir au menu principal4
            elif choix == '5':
                print("Liste des titres de livres disponibles par ordre alphabétique :")
                sorted_titles = sorted([livre.titre for livre in self.bibliotheque.livres])
                for title in sorted_titles:
                    print(f"- {title}")

                titre = input("Entrez le titre du livre à supprimer : ")
                livre = next((l for l in self.bibliotheque.livres if l.titre == titre), None)
                if livre:
                    self.bibliotheque.supprimer_livre(livre)
                    print("Livre supprimé avec succès.")
                    input()
                else:
                    print("Livre non trouvé.")
            elif choix == '6':
                print("Liste des livres :")
                print("{:<30} {:<15} {:<10} {:<15}".format("Titre", "ISBN", "Emprunté", "Date d'emprunt"))

                for livre in self.bibliotheque.livres:
                    emprunte = 'Non'
                    date_emprunt = 'Non emprunté'

                    for emprunt in self.bibliotheque.emprunts:
                        if emprunt.livre == livre:
                            if emprunt.date_retour is None:
                                emprunte = 'Oui'
                                date_emprunt = emprunt.date_emprunt
                            else:
                                emprunte = 'Non'
                                date_emprunt = 'Non emprunté'
                            break

                    print("{:<30} {:<15} {:<10} {:<15}".format(livre.titre, livre.ISBN, emprunte, date_emprunt))

                input()

            elif choix == '7':
                numAdherent = input("Entrez le ID de l'adhérent qui emprunte : ")
                adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                if not adherent:
                    print("Adhérent non trouvé.")
                    continue

                livres_empruntes = [emprunt.livre for emprunt in self.bibliotheque.emprunts if
                                    emprunt.adherent == adherent]

                if livres_empruntes:
                    print(f"Liste des livres empruntés par {adherent.nom} {adherent.prenom} :")
                    print("{:<30} {:<15} {:<15}".format("Titre", "ISBN", "Date d'emprunt"))
                    for livre in livres_empruntes:
                        date_emprunt = next((emprunt.date_emprunt for emprunt in self.bibliotheque.emprunts if
                                             emprunt.livre == livre and emprunt.adherent == adherent), "Non emprunté")
                        print("{:<30} {:<15} {:<15}".format(livre.titre, livre.ISBN, date_emprunt))
                else:
                    print("Cet adhérent n'a emprunté aucun livre.")
                titre = input("Entrez le titre du livre emprunté : ")
                livre = next((l for l in self.bibliotheque.livres if l.titre == titre), None)
                if not livre:
                    print("Livre non trouvé.")
                    continue

                date_emprunt = datetime.datetime.now().strftime("%Y-%m-%d")
                emprunt = Emprunt(adherent, livre, date_emprunt)
                self.bibliotheque.ajouter_emprunt(emprunt)
                print("Emprunt exécuté avec succès")
                input()
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
                print("Liste des Emprunts :")
                print("Adhérent".ljust(20), "Livre".ljust(30), "Date d'emprunt")
                for emprunt in self.bibliotheque.emprunts:
                    if emprunt.date_retour is None:
                        print(f"{emprunt.adherent.nom} {emprunt.adherent.prenom}".ljust(20), f"{emprunt.livre.titre}".ljust(30), f"{emprunt.date_emprunt}")
                input()
            else:
                print("Choix invalide, veuillez réessayer.")

bibliotheque = Bibliotheque()
interface = InterfaceUtilisateur(bibliotheque)
interface.run()
