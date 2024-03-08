from models.config import session
from models.models import User
from views.users import UserView
from .authentication import AuthenticationController
from utils.decorators import login_required, manager_required


class UserController:
    # On fait ce init pour écrire ce qu'il y a à gauche du égal à la place de ce qu'il y a à droite
    def __init__(self):
        self.user_view = UserView()
        self.auth_controller = AuthenticationController()

    @login_required
    @manager_required
    def create_user(self):
        username, password, role = self.user_view.get_user_data()
        new_user = User(
            username=username,
            password=password,
            role=role
        )
        new_user.set_password(password)
        session.add(new_user)
        session.commit()
        return new_user

    @login_required
    def display_users(self):
        users = session.query(User).all()
        self.user_view.display_users(users)

    @login_required
    @manager_required
    def update_user(self):
        self.display_users()
        users = session.query(User).all()
        user_id_list = [user.id for user in users]
        user_id = self.user_view.get_user_id(user_id_list)
        user = session.query(User).filter_by(id=user_id).first()
        username, password = self.user_view.update_user(user)
        user.username = username
        if password:
            user.password = password
            user.set_password(password)
        session.commit()

    @login_required
    @manager_required
    def delete_user(self):
        self.display_users()
        users = session.query(User).all()
        user_id_list = [user.id for user in users]
        user_id = self.user_view.get_user_id(user_id_list)
        user = session.query(User).filter_by(id=user_id).first()
        session.delete(user)
        session.commit()
