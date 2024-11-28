from database import Database
from note import Note

class Notebook:
    """Classe pour gérer les notes via la base de données."""
    
    def __init__(self, db):
        self.db = db

    def add_note(self, content, tags=None):
        """Ajoute une nouvelle note au carnet."""
        tags = tags or []
        self.db.add_note(content, tags)

    def modify_note(self, note_id, new_content=None, new_tags=None):
        """Modifie une note existante par son identifiant."""
        note_data = self.db.search_notes(str(note_id))
        if note_data:
            current_content, current_tags, _ = note_data[0][1], note_data[0][2], note_data[ 0][3]
            new_content = new_content if new_content else current_content
            new_tags = new_tags if new_tags else current_tags.split(',')
            self.db.modify_note(note_id, new_content, new_tags)

    def search_notes(self, search_term):
        """Recherche des notes correspondant à un terme de recherche."""
        return self.db.search_notes(search_term)

    def display_notes(self):
        """Affiche toutes les notes dans le carnet."""
        notes = self.db.display_notes()
        return [Note(note[0], note[1], note[2].split(',')) for note in notes]

    def close(self):
        """Ferme la connexion à la base de données."""
        self.db.close()