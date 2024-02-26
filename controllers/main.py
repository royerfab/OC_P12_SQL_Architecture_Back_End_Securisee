from views import MenuView
from .users import UserController
from .clients import ClientController
from .contracts import ContractController
from .events import EventController
from .authentication import AuthenticationController




class MainController:
    def __init__(self):
        self.menu_view = MenuView()
        self.user_controller = UserController()
        self.client_controller = ClientController()
        self.contract_controller = ContractController()
        self.event_controller = EventController()
        self.auth_controller = AuthenticationController()
    
    def start(self):
        choice = self.menu_view.main_menu()
        if choice == 1:
            self.user_manager()
        elif choice == 2:
            self.client_manager()
        elif choice == 3:
            self.contract_manager()
        elif choice == 4:
            self.event_manager()
        elif choice == 5:
            self.auth_controller.login()
        elif choice == 6:
            self.auth_controller.logout()

    def user_manager(self):
        choice = self.menu_view.user_menu()
        if choice == 1:
            self.user_controller.create_user()
        elif choice == 2:
            self.user_controller.update_user()
        elif choice == 3:
            self.user_controller.delete_user()
        elif choice == 4:
            self.user_controller.display_users()

    def client_manager(self):
        choice = self.menu_view.client_menu()
        if choice == 1:
            self.user_controller.create_client()
        elif choice == 2:
            self.user_controller.update_client()
        elif choice == 3:
            self.user_controller.delete_client()
        elif choice == 4:
            self.user_controller.display_clients()

    def contract_manager(self):
        choice = self.menu_view.contract_menu()
        if choice == 1:
            self.user_controller.create_contract()
        elif choice == 2:
            self.user_controller.update_contract()
        elif choice == 3:
            self.user_controller.delete_contract()
        elif choice == 4:
            self.user_controller.display_contracts()

    def event_manager(self):
        choice = self.menu_view.event_menu()
        if choice == 1:
            self.user_controller.create_event()
        elif choice == 2:
            self.user_controller.update.event()
        elif choice == 3:
            self.user_controller.delete_event()
        elif choice == 4:
            self.user_controller.display_events()