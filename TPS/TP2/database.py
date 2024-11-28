import sqlite3
import datetime

class Database:
    """Classe pour gérer la connexion à la base de données et les opérations CRUD."""
    
    def __init__(self, db_name='notebook.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Crée la table des notes si elle n'existe pas déjà."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    tags TEXT,
                    date_created TEXT NOT NULL
                )
            ''')

    def add_note(self, content, tags):
        """Ajoute une nouvelle note à la base de données."""
        date_created = datetime.datetime.now().isoformat()
        with self.connection:
            self.connection.execute('''
                INSERT INTO notes (content, tags, date_created) VALUES (?, ?, ?)
            ''', (content, ','.join(tags), date_created))

    def modify_note(self, note_id, new_content, new_tags):
        """Modifie une note existante par son identifiant."""
        with self.connection:
            self.connection.execute('''
                UPDATE notes SET content = ?, tags = ? WHERE id = ?
            ''', (new_content, ','.join(new_tags), note_id))

    def search_notes(self, search_term):
        """Recherche des notes correspondant à un terme de recherche."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM notes WHERE content LIKE ? OR tags LIKE ?
        ''', (f'%{search_term}%', f'%{search_term}%'))
        return cursor.fetchall()

    def display_notes(self):
        """Affiche toutes les notes dans la base de données."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM notes')
        return cursor.fetchall()

    def close(self):
        """Ferme la connexion à la base de données."""
        self.connection.close()