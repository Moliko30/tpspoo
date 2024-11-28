class Authorizor:
    """Classe pour gérer les autorisations des utilisateurs."""
    
    def __init__(self):
        self.permissions = {}

    def grant_permission(self, username, permission):
        """Accorde une permission à un utilisateur."""
        if username not in self.permissions:
            self.permissions[username] = set()
        self.permissions[username].add(permission)

    def revoke_permission(self, username, permission):
        """Révoque une permission d'un utilisateur."""
        if username in self.permissions:
            self.permissions[username].discard(permission)

    def is_authorized(self, username, permission):
        """Vérifie si un utilisateur a une permission spécifique."""
        return permission in self.permissions.get(username, set())