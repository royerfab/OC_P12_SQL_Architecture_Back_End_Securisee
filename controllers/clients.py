from models.config import session
from models.models import Client
from views.clients import ClientView
from utils.decorators import login_required, manager_required, sales_required
from .authentication import AuthenticationController


class ClientController:
    def __init__(self):
        self.client_view = ClientView()
        self.auth_controller = AuthenticationController()

    #Associe automatiquement un commercial au client qu'il a créé en utilisant get_current_user pour le sales_contact_id.
    @login_required
    @sales_required
    def create_client(self):
        (
            name,
            email,
            phone,
            company_name,
        ) = self.client_view.get_client_data()

        current_user = self.auth_controller.get_current_user()
        sales_contact_id = current_user.id

        new_client = Client(
            name=name,
            email=email,
            phone=phone,
            company_name=company_name,
            sales_contact_id=sales_contact_id
        )
        session.add(new_client)
        session.commit()

    @login_required
    def display_clients(self):
        clients = session.query(Client).all()
        self.client_view.display_clients(clients)

    #Affiche les clients d'un commercial.
    @login_required
    @sales_required
    def display_my_clients(self):
        current_user = self.auth_controller.get_current_user()
        clients = session.query(Client).filter_by(sales_contact_id=current_user.id)
        if clients.count() >0:
            self.client_view.display_clients(clients)
            return clients
        else:
            return None

    # Permet de voir les clients d'un commercial pour qu'il soit le seul à les modifier en utilisant display_my_clients.
    # On peut également avoir la liste des id des clients pour ne pas sélectionner un un id n'existant pas dans get_client_id.
    @login_required
    @sales_required
    def update_client(self):
        clients = self.display_my_clients()
        if clients:
            client_id_list = [client.id for client in clients]
            client_id = self.client_view.get_client_id(client_id_list)
            client = session.query(Client).filter_by(id=client_id).first()
            (
                name,
                email,
                phone,
                company_name,
            ) = self.client_view.update_client(client)
            client.name = name
            client.email = email
            client.phone = phone
            client.company_name = company_name
            session.commit()
        else:
            print("Vous n'avez pas de client")

    @login_required
    @manager_required
    def delete_client(self):
        self.display_clients()
        client_id = self.client_view.get_client_id()
        client = session.query(Client).filter_by(id = client_id).first()
        session.delete(client)
        session.commit()

