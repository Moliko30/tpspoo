import sys
from database import Database
from notebook import Notebook

def main():
    db = Database()
    notebook = Notebook(db)

    while True:
        print("\nMenu:")
        print("1. Ajouter une note")
        print("2. Modifier une note")
        print("3. Rechercher des notes")
        print("4. Afficher toutes les notes")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            content = input("Entrez le contenu de la note: ")
            tags = input("Entrez des balises (séparées par des virgules): ").split(',')
            notebook.add_note(content, tags)
            print("Note ajoutée avec succès.")

        elif choice == '2':
            note_id = input("Entrez l'ID de la note à modifier: ")
            new_content = input("Entrez le nouveau contenu (laisser vide pour ne pas changer): ")
            new_tags = input("Entrez de nouvelles balises (séparées par des virgules, laisser vide pour ne pas changer): ").split(',')
            notebook.modify_note(note_id, new_content if new_content else None, new_tags if new_tags[0] else None)
            print("Note modifiée avec succès.")

        elif choice == '3':
            search_term = input("Entrez le terme de recherche: ")
            results = notebook.search_notes(search_term)
            for note in results:
                print(note)

        elif choice == '4':
            notes = notebook.display_notes()
            for note in notes:
                print(note)

        elif choice == '5':
            notebook.close()
            print("Au revoir!")
            sys.exit()

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()