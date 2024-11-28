from authenticator import Authenticator
from authorizor import Authorizor
from auth_exceptions import AuthException

def main():
    authenticator = Authenticator()
    authorizor = Authorizor()

    while True:
        print("\n=== Système d'Authentification et d'Autorisation ===")
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Vérifier les permissions")
        print("4. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            username = input("Entrez un nom d'utilisateur: ")
            password = input("Entrez un mot de passe: ")
            try:
                authenticator.add_user(username, password)
                print(f"L'utilisateur {username} a été ajouté avec succès.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            username = input("Entrez votre nom d'utilisateur: ")
            password = input("Entrez votre mot de passe: ")
            try:
                user = authenticator.login(username, password)
                print(f"{user.username} est connecté.")
            except AuthException as e:
                print(e)

        elif choice == '3':
            username = input("Entrez votre nom d'utilisateur: ")
            action = input("Entrez l'action à vérifier (ex: edit_post): ")
            if authorizor.is_authorized(action, username):
                print(f"{username} est autorisé à effectuer l'action '{action}'.")
            else:
                print(f"{username} n'est pas autorisé à effectuer l'action '{action}'.")

        elif choice == '4':
            print("Au revoir!")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()