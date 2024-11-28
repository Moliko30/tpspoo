import hashlib

class User:
    """Classe représentant un utilisateur."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        """Hache le mot de passe pour le stocker de manière sécurisée."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Vérifie si le mot de passe fourni correspond au mot de passe stocké."""
        return self.password_hash == self._hash_password(password)