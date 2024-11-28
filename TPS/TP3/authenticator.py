from user import User
from auth_exceptions import UserNotFoundException, InvalidPasswordException

class Authenticator:
    """Classe pour gérer l'authentification des utilisateurs."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """Enregistre un nouvel utilisateur."""
        if username in self.users:
            raise UserNotFoundException(username)
        self.users[username] = User(username, password)

    def authenticate(self, username, password):
        """Authentifie un utilisateur."""
        if username not in self.users:
            raise UserNotFoundException(username)
        user = self.users[username]
        if not user.check_password(password):
            raise InvalidPasswordException(username)
        return user