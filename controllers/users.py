from models.config import session
from models.models import User
from views.users import UserView


class UserController:
    # On fait ce init pour écrire ce qu'il y a à gauche du égal à la place de ce qu'il y a à droite
    def __init__(self):
        self.user_view = UserView()

    def create_user(self):
        username, password, role = self.user_view.get_user_data()
        new_user = User(
            username = username,
            password = password,
            role = role
        )
        session.add(new_user)
        session.commit()

    def display_users(self):
        users = session.query(User).all()
        self.user_view.display_users(users)

    def update_user(self):
        self.display_users()
        user_id = self.user_view.get_user_id()
        user = session.query(User).filter_by(id = user_id).first()
        username, password, role = self.user_view.update_user(user)
        user.username = username
        user.role = role
        if password:
            user.password = password
        session.commit()
