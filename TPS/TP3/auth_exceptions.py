class AuthException(Exception):
    """Classe de base pour toutes les exceptions d'authentification."""
    def __init__(self, username, message):
        super().__init__(message)
        self.username = username

class UserNotFoundException(AuthException):
    """Exception levée lorsque l'utilisateur n'est pas trouvé."""
    def __init__(self, username):
        super().__init__(username, f"L'utilisateur '{username}' n'a pas été trouvé.")

class InvalidPasswordException(AuthException):
    """Exception levée lorsque le mot de passe est invalide."""
    def __init__(self, username):
        super().__init__(username, "Le mot de passe est invalide.")

class UserAlreadyExistsException(AuthException):
    """Exception levée lorsque l'utilisateur existe déjà."""
    def __init__(self, username):
        super().__init__(username, f"L'utilisateur '{username}' existe déjà.")