import csv
import datetime
# Définition des classes
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

# Classe décrivant un adhérent avec un identifiant unique
class Adherent(Personne):
    def __init__(self, p, numAdherent):
        super().__init__(p.nom, p.prenom, p.age)
        self.numAdherent = numAdherent

    def __eq__(self, other):
        return self.numAdherent == other.numAdherent

# Classe de base pour tout type de document
class Document:
    def __init__(self, titre, nombrePages, ISBN):
        self.titre = titre
        self.nombrePages = nombrePages
        self.ISBN = ISBN

# Classe spécifique pour les livres, héritant de la classe Document
class Livre(Document):
    def __init__(self, doc, Auteur, maisonEdition, emprunte=False):
        super().__init__(doc.titre, doc.nombrePages, doc.ISBN)
        self.emprunte = emprunte
        self.Auteur = Auteur
        self.maisonEdition = maisonEdition

# Classe représentant un emprunt associant un adhérent à un livre et des dates
class Emprunt:
    def __init__(self, adherent, livre, date_emprunt, date_retour=None):
        self.adherent = adherent
        self.livre = livre
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour

# Classe gérant les opérations de la bibliothèque : ajout, suppression, sauvegarde, etc.
class Bibliotheque:
    def __init__(self):
        self.adherents = []
        self.livres = []
        self.emprunts = []

    def sauvegarder_livres(self, filename="livres.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["titre", "nombrePages", "ISBN", "auteur", "maisonEdition", "emprunte"])

            for livre in self.livres:
                writer.writerow(
                    [livre.titre, livre.nombrePages, livre.ISBN, livre.Auteur, livre.maisonEdition, livre.emprunte])

    def sauvegarder_adherents(self, filename="adherents.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nom", "prenom", "age", "numAdherent"])

            for adherent in self.adherents:
                writer.writerow([adherent.nom, adherent.prenom, adherent.age, adherent.numAdherent])

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)
        self.sauvegarder_adherents("adherents.csv")

    def supprimer_adherent(self, adherent):
        self.adherents.remove(adherent)
        self.sauvegarder_adherents("adherents.csv")

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        self.sauvegarder_livres("livres.csv")

    def supprimer_livre(self, livre):
        self.livres.remove(livre)
        self.sauvegarder_livres("livres.csv")

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
            input()
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
        ╔══════════════════════════════════════════════╗
        ║═══════ Bienvenue à votre Bibliothèque ═══════║
        ╠═══════════════ Faite un choix ═══════════════╣                
        ╟ 1  →      Ajouter adhérent                   ║  
        ╟ 2  →      Supprimer adhérent                 ║  
        ╟ 3  →      Afficher tous les adhérents        ║  
        ╟ 4  →      Ajouter Livre                      ║  
        ╟ 5  →      Supprimer Livre                    ║  
        ╟ 6  →      Afficher tous les Livres           ║  
        ╟ 7  →      Ajouter Emprunt                    ║  
        ╟ 8  →      Retour d’un Emprunt                ║  
        ╟ 9  →      Afficher tous les Emprunts         ║  
        ╟ Q  →      Quitter                            ║  
        ╚══════════════════════════════════════════════╝
        """)

    def run(self):
        while True:
            self.menu()
            choix = input("Choisissez une action : ")

            if choix.lower() == 'q':
                print("Merci d'avoir utilisé notre bibliothèque. À bientôt !")
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
                print("Adhérent supprimé avec succès")
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
                while True:
                    print("Liste des livres disponibles :\n")
                    print("{:<5} {:<30} {:<15} {:<15} {:<20} {:<20} {:<10}".format("Num", "Titre", "ISBN", "Emprunté",
                                                                                   "Auteur", "Maison d'édition",
                                                                                   "Nombre de pages"))

                    for idx, livre in enumerate(self.bibliotheque.livres, start=1):
                        emprunte = 'Non'
                        for emprunt in self.bibliotheque.emprunts:
                            if emprunt.livre == livre and emprunt.date_retour is None:
                                emprunte = 'Oui'
                                break

                        print("{:<5} {:<30} {:<15} {:<15} {:<20} {:<20} {:<10}".format(
                            idx, livre.titre, livre.ISBN, emprunte, livre.Auteur, livre.maisonEdition,
                            livre.nombrePages))

                    print("\nSaisissez le numéro du livre à supprimer (ou 'Q' pour revenir au menu principal) : ")
                    user_input = input()

                    if user_input.lower() == 'q':
                        break

                    try:
                        user_choice = int(user_input)
                        if 1 <= user_choice <= len(self.bibliotheque.livres):
                            livre = self.bibliotheque.livres[user_choice - 1]
                            self.bibliotheque.supprimer_livre(livre)
                            print("\n------------------------------")
                            print("Livre supprimé avec succès.")
                            input("Appuyez sur Entrée pour continuer...")
                        else:
                            print("------------------------------")
                            print("Choix invalide. Veuillez saisir un numéro de livre valide.")
                    except ValueError:
                        print("------------------------------")
                        print("Veuillez saisir un numéro valide ou 'Q' pour revenir au menu principal.")
            elif choix == '6':
                print("Liste des livres :")
                print("{:<30} {:<15} {:<10} {:<15} {:<20} {:<20} {:<10}".format("Titre", "ISBN", "Emprunté",
                                                                                "Auteur", "Maison d'édition",
                                                                                "Nombre de pages", "Date d'emprunt"))

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

                    print("{:<30} {:<15} {:<10} {:<15} {:<20} {:<20} {:<10}".format(livre.titre, livre.ISBN, emprunte,
                                                                                    livre.Auteur, livre.maisonEdition,
                                                                                    livre.nombrePages, date_emprunt))
                input()
            elif choix == '7':
                while True:
                    print("\nListe des adhérents :")
                    print("{:<20} {:<20} {:<10}".format("ID", "Nom", "Prénom"))
                    for adherent in self.bibliotheque.adherents:
                        print("{:<20} {:<20} {:<10}".format(adherent.numAdherent, adherent.nom, adherent.prenom))
                    print("\n(Ou tapez 'Q' pour revenir au menu principal)")

                    numAdherent = input("Entrez l'ID de l'adhérent qui emprunte : ")
                    if numAdherent.lower() == 'q':
                        break

                    adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                    if not adherent:
                        print("Adhérent non trouvé.")
                        continue

                    print("\nListe des livres disponibles :")
                    print("{:<5} {:<30} {:<15} {:<15} {:<20} {:<20} {:<10}".format(
                        "Num", "Titre", "ISBN", "Emprunté", "Auteur", "Maison d'édition", "Nombre de pages"))
                    for idx, livre in enumerate(self.bibliotheque.livres, start=1):
                        emprunte = 'Non'
                        for emprunt in self.bibliotheque.emprunts:
                            if emprunt.livre == livre and emprunt.date_retour is None:
                                emprunte = 'Oui'
                                break
                        print("{:<5} {:<30} {:<15} {:<15} {:<20} {:<20} {:<10}".format(
                            idx, livre.titre, livre.ISBN, emprunte, livre.Auteur, livre.maisonEdition,
                            livre.nombrePages))

                    print("\n(Ou tapez 'Q' pour revenir au menu principal)")

                    ISBN = input("Entrez l'ISBN du livre emprunté : ")
                    if ISBN.lower() == 'q':
                        break

                    livre = next((l for l in self.bibliotheque.livres if l.ISBN == ISBN and not l.emprunte), None)
                    if not livre:
                        print("Livre non trouvé ou déjà emprunté.")
                        continue

                    date_emprunt = datetime.datetime.now().strftime("%Y-%m-%d")
                    emprunt = Emprunt(adherent, livre, date_emprunt)
                    self.bibliotheque.ajouter_emprunt(emprunt)
                    print("Emprunt effectué avec succès")
                    livre.emprunte = True

                    autre_emprunt = input("Voulez-vous ajouter un autre livre à emprunter ? (Oui/Non) : ").lower()
                    if autre_emprunt == 'oui':
                        continue
                    elif autre_emprunt == 'non':
                        break
                    elif autre_emprunt == 'q':
                        break
            elif choix == '8':
                while True:
                    print("Liste des adhérents :")
                    print("{:<20} {:<20} {:<10}".format("ID", "Nom", "Prénom"))
                    for adherent in self.bibliotheque.adherents:
                        print("{:<20} {:<20} {:<10}".format(adherent.numAdherent, adherent.nom, adherent.prenom))
                    print("\n(Ou tapez 'Q' pour revenir au menu principal)")

                    numAdherent = input("Entrez le ID de l'adhérent qui retourne le livre : ")
                    if numAdherent.lower() == 'q':
                        return

                    adherent = next((a for a in self.bibliotheque.adherents if a.numAdherent == numAdherent), None)
                    if not adherent:
                        print("Adhérent non trouvé.")
                        continue

                    print("\nListe des livres empruntés par l'adhérent :")
                    print("{:<5} {:<30} {:<15} {:<10}".format("Num", "Titre", "ISBN", "Emprunté"))
                    for idx, emprunt in enumerate(self.bibliotheque.emprunts, start=1):
                        if emprunt.adherent == adherent and emprunt.date_retour is None:
                            livre = emprunt.livre
                            print("{:<5} {:<30} {:<15} {:<10}".format(idx, livre.titre, livre.ISBN,
                                                                      "Oui" if livre.emprunte else "Non"))

                    print("\n(Ou tapez 'Q' pour revenir au menu principal)")

                    ISBN = input("Entrez l'ISBN du livre à retourner : ")
                    if ISBN.lower() == 'q':
                        return

                    livre = next((l for l in self.bibliotheque.livres if l.ISBN == ISBN and l.emprunte), None)
                    if not livre:
                        print("Livre non trouvé ou déjà retourné.")
                        continue

                    emprunt = next(
                        (e for e in self.bibliotheque.emprunts if e.livre == livre and e.date_retour is None), None)
                    if not emprunt:
                        print("Emprunt non trouvé.")
                        continue

                    self.bibliotheque.retourner_emprunt(emprunt)
                    livre.emprunte = False
                    print("Retour effectué avec succès")

                    # Mise à jour de la liste des livres après le retour
                    print("\nListe des livres après le retour :")
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
                    break  # Sortie de la boucle une fois que le retour est effectué et la liste des livres mise à jour

            elif choix == '9':
                print("Liste des Emprunts :")
                print("Adhérent".ljust(20), "Livre".ljust(30), "Date d'emprunt")
                for emprunt in self.bibliotheque.emprunts:
                    if emprunt.date_retour is None:
                        print(f"{emprunt.adherent.nom} {emprunt.adherent.prenom}".ljust(20), f"{emprunt.livre.titre}".ljust(30), f"{emprunt.date_emprunt}")
                input()
            else:
                print("Choix invalide, veuillez réessayer.")
                input()

bibliotheque = Bibliotheque()
interface = InterfaceUtilisateur(bibliotheque)
interface.run()
