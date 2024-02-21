from views.menu import MenuView
from .users import UserController



class MainController:
    def __init__(self):
        self.menu_view = MenuView()
        self.user_controller = UserController()
    
    def start(self):
        choice = self.menu_view.main_menu()
        if choice == 1:
            self.user_manager()

    def user_manager(self):
        choice = self.menu_view.user_menu()
        if choice == 1:
            self.user_controller.create_user()
        elif choice == 2:
            self.user_controller.update_user()
        elif choice == 4:
            self.user_controller.display_users()

        