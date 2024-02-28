from .errorview import InputCheckView
from rich.console import Console
from rich.table import Table


class ClientView:
    def __init__(self):
        self.input = InputCheckView()

    def get_client_data(self):
        first_and_last_name = self.input.check_string("Entrer le nom et prénom du client : ")
        email = input("Entrer l'email du client : ")
        phone_number = self.input.check_string("Entrer le numéro de téléphone du client : ")
        company_name = self.input.check_string("Entrer le nom de l'entreprise du client : ")
        return first_and_last_name, email, phone_number, company_name
            
    def display_clients(self, clients):
        table = Table(title = "Liste des clients")
        table.add_column("Client id")
        table.add_column("Name")
        table.add_column("Email")
        table.add_column("Phone")
        table.add_column("Company name")
        table.add_column("Created at")
        table.add_column("Last contact")
        table.add_column("Sales contact")
      
        for client in clients:
            table.add_row(str(client.id), str(client.name), str(client.email), str(client.phone),
                          str(client.company_name), str(client.created_at), str(client.last_contact), str(client.sales_contact))

        console = Console()
        console.print(table)
    
    def get_client_id(self, client_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du client concerné : ", client_id_list)
        return choice

    def update_client(self, client):
        print("Taper Entrée pour conserver la valeur sans modification")
        first_and_last_name = self.input.check_string(f"Nom et prénom ({client.name}) : ", updated=True) or client.name
        email = self.input.check_string(f"Email ({client.email}) : ", updated=True) or client.email
        phone_number = self.input.check_string(f"Numéro de téléphone ({client.phone}) : ", updated=True) or client.phone
        company_name = self.input.check_string(f"Nom de l'entreprise ({client.company_name}) : ", updated=True) or client.company_name
        return first_and_last_name, email, phone_number, company_name