from models.config import session
from models.models import Client
from views.clients import ClientView
from utils.decorators import login_required, manager_required, sales_required


class ClientController:
    def __init__(self):
        self.client_view = ClientView()

    @login_required
    @sales_required
    def create_client(self):
        (
            first_and_last_name,
            email,
            phone_number,
            company_name,
            creation_date,
            last_update,
            sales_person,
        ) = self.client_view.get_client_data()
        new_client = Client(
            first_and_last_name=first_and_last_name,
            email=email,
            phone_number=phone_number,
            company_name=company_name,
            creation_date=creation_date,
            last_update=last_update,
            sales_person=sales_person,
        )
        session.add(new_client)
        session.commit()

    @login_required
    def display_clients(self):
        clients = session.query(Client).all()
        self.client_view.display_clients(clients)

    @login_required
    @sales_required
    def update_client(self):
        self.display_clients()
        client_id = self.client_view.get_client_id()
        client = session.query(Client).filter_by(id=client_id).first()
        (
            first_and_last_name,
            email,
            phone_number,
            company_name,
            creation_date,
            last_update,
            sales_person,
        ) = self.client_view.update_client(client)
        client.first_and_last_name = first_and_last_name
        client.email = email
        client.phone_number = phone_number
        client.company_name = company_name
        client.creation_date = creation_date
        client.last_update = last_update
        client.sales_person = sales_person
        session.commit()

    @login_required
    @manager_required
    def delete_client(self):
        self.display_clients()
        client_id = self.client_view.get_client_id()
        client = session.query(Client).filter_by(id = client_id).first()
        session.delete(client)
        session.commit()

