from .errorview import InputCheckView


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
        for client in clients:
            print(client.id, "-", client.name, "-", client.email, "-", client.phone, "-", client.company_name,
                   "-", client.created_at, "-", client.last_contact, "-", client.sales_contact)
    
    def get_client_id(self, client_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du client concerné : ", client_id_list)
        return choice
    #pourquoi les or?
    def update_client(self, client):
        print("Taper Entrée pour conserver la valeur sans modification")
        first_and_last_name = self.input.check_string(f"Nom et prénom ({client.name}) : ", updated=True) or client.name
        email = self.input.check_string(f"Email ({client.email}) : ", updated=True) or client.email
        phone_number = self.input.check_string(f"Numéro de téléphone ({client.phone}) : ", updated=True) or client.phone
        company_name = self.input.check_string(f"Nom de l'entreprise ({client.company_name}) : ", updated=True) or client.company_name
        return first_and_last_name, email, phone_number, company_name