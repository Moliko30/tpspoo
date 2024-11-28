import datetime

class Note:
    """Classe représentant une note."""
    
    def __init__(self, note_id, content, tags=None):
        """Initialise une nouvelle note avec un ID, du contenu et des balises."""
        self.id = note_id
        self.content = content
        self.tags = tags if tags else []
        self.date_created = datetime.datetime.now()

    def modify_content(self, new_content):
        """Modifie le contenu de la note."""
        self.content = new_content

    def modify_tags(self, new_tags):
        """Modifie les balises de la note."""
        self.tags = new_tags

    def matches(self, search_term):
        """Vérifie si la note correspond à un terme de recherche."""
        return (search_term.lower() in self.content.lower() or
                any(search_term.lower() in tag.lower() for tag in self.tags))

    def __str__(self):
        """Représentation de la note sous forme de chaîne."""
        return f"[{self.date_created.strftime('%Y-%m-%d %H:%M:%S')}] {self.content} (Tags: {', '.join(self.tags)})"