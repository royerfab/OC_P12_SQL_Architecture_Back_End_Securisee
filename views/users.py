
class UserView:
    def get_user_data(self):
        username = input("Entrer le nom d'utilisateur : ")
        password = input("Entrer le mot de passe : ")
        role = input("Entrer le rôle : ")
        return username, password, role
    
    def display_users(self, users):
        for user in users:
            print(user.id, "-", user.username)
    
    def get_user_id(self):
        choice = int(input("Entrer l'id de l'utilisateur concerné : "))
        return choice
    
    def update_user(self, user):
        print("taper Entrée pour conserver la valeur sans modification")
        username = input(f"usernanme ({user.username}) : ") or user.username
        password = input(f"password (****) : ")
        role = input(f"role ({user.role}) : ") or user.role
        return username, password, role

