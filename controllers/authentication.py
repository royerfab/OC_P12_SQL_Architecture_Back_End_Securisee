from views import AuthenticationView
from models.models import User
from models.config import session
import pickle
import os
from models.models import RoleEnum


class AuthenticationController:
    KEY_FILE = "key.pkl"

    def __init__(self):
        self.auth_view = AuthenticationView()

    def login(self):
        current_user = self.get_current_user()
        if current_user:
            print("Vous êtes déjà connecté")
        else:
            username, password = self.auth_view.get_login_data()
            user = session.query(User).filter_by(username=username).first()
            if user:
                print("L'utilisateur existe")
                if user.check_password(password):
                    self.save_login_key(user)
                else:
                    print("invalid password")
            else:
                print("user does not exist")

    # On note l'id de l'utilisateur dans ce fichier d'authentification
    def save_login_key(self, user):
        with open(self.KEY_FILE, "wb") as file:
            pickle.dump(user.id, file)

    def get_current_user(self):  # Verifier et Charger si user est auhthentifié
        try:
            with open(self.KEY_FILE, "rb") as file:  # rb lecture
                user_id = pickle.load(file)  # Lecture contenu du fichier (id)
                if user_id:
                    user = session.query(User).filter_by(id=user_id).one()
                    return user
                else:
                    return None
        except FileNotFoundError:
            return None
        # except FileNotFoundError as e:
            # sentry_sdk.capture_exception(e)

    def logout(self):
        if os.path.exists(self.KEY_FILE):
            os.remove(self.KEY_FILE)

    def is_manager(self):
        current_user = self.get_current_user()
        if current_user and current_user.role == RoleEnum.GESTION.value:
            return current_user
        return None

    def is_sales_person(self):
        current_user = self.get_current_user()
        if current_user and current_user.role == RoleEnum.COMMERCIAL.value:
            return current_user
        return None

    def is_support(self):
        current_user = self.get_current_user()
        if current_user and current_user.role == RoleEnum.SUPPORT.value:
            return current_user
        return None

    def is_sales_or_manager(self):
        return self.is_manager() or self.is_sales_person()
