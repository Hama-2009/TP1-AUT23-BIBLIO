def add_adherent():
    print("Fonctionnalité pour ajouter un adhérent.")

def delete_adherent():
    print("Fonctionnalité pour supprimer un adhérent.")

def list_adherents():
    print("Fonctionnalité pour lister tous les adhérents.")

def add_document():
    print("Fonctionnalité pour ajouter un document.")

def delete_document():
    print("Fonctionnalité pour supprimer un document.")

def list_documents():
    print("Fonctionnalité pour lister tous les documents.")

def add_loan():
    print("Fonctionnalité pour ajouter un emprunt.")

def return_loan():
    print("Fonctionnalité pour retourner un emprunt.")

def list_loans():
    print("Fonctionnalité pour lister tous les emprunts.")

def quit_program():
    print("Merci d'avoir utilisé notre programme.")
    return True


def menu():
    while True:
        print("\n******** Bienvenue à votre bibliothèque ********")
        print("1       Ajouter adhérent")
        print("2       Supprimer adhérent")
        print("3       Afficher tous les adhérents")
        print("4       Ajouter Document")
        print("5       Supprimer Document")
        print("6       Afficher tous les Documents")
        print("7       Ajouter Emprunts")
        print("8       Retour d’un Emprunts")
        print("9       Afficher tous les Emprunts")
        print("Q      Quitter")

        action = input("Choisissez une action : ")

        if action == '1':
            add_adherent()
        elif action == '2':
            delete_adherent()
        elif action == '3':
            list_adherents()
        elif action == '4':
            add_document()
        elif action == '5':
            delete_document()
        elif action == '6':
            list_documents()
        elif action == '7':
            add_loan()
        elif action == '8':
            return_loan()
        elif action == '9':
            list_loans()
        elif action.lower() == 'q':
            if quit_program():
                break
        else:
            print("Action non valide, veuillez réessayer.")