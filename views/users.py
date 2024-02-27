#Utiliser les static method, décorateur au dessus pour ne pas utiliser self
#reprendre les __str__ pour le print de user

#demander le nom de l'utilisateur, retrouver son id
from .errorview import InputCheckView


class UserView:
    def __init__(self):
        self.input = InputCheckView()

    # staticmethod : plus accès aux input check 
    def get_user_data(self):
        username = self.input.check_string("Entrer le nom d'utilisateur : ")
        password = self.input.check_string("Entrer le mot de passe : ")
        role = self.input.role_option()
        return username, password, role
    
    def display_users(self, users):
        for user in users:
            print(user)

    
    def get_user_id(self, user_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id de l'utilisateur concerné : ", user_id_list)
        return choice
    #Pourquoi les or?
    def update_user(self, user):
        print("Taper Entrée pour conserver la valeur sans modification")
        username = self.input.check_string(f"usernanme ({user.username}) : ", updated=True) or user.username
        password = self.input.check_string(f"password (****) : ")
        role = self.input.role_option() or user.role
        return username, password, role

