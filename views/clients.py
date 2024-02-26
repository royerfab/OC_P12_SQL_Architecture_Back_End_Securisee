from .errorview import InputCheckView


class ClientView:
    def __init__(self):
        self.input = InputCheckView()

    def get_client_data(self):
        first_and_last_name = self.input.check_string("Entrer le nom et prénom du client : ")
        email = input("Entrer l'email du client : ")
        phone_number = self.input.check_int("Entrer le numéro de téléphone du client : ")
        company_name = self.input.check_string("Entrer le nom de l'entreprise du client : ")
        creation_date = self.input.check_date("Entrer la date de création du client : ")
        last_update = self.input.check_date("Entrer la date de dernière mise à jour du client : ")
        sales_person = self.input.check_string("Entrer le nom du commercial associé au client : ")
        return first_and_last_name, email, phone_number, company_name, creation_date, last_update, sales_person
    
    def display_clients(self, clients):
        for client in clients:
            print(client.id, "-", client.first_and_last_name, "-", client.email, "-", client.phone_number, "-", client.company_name,
                   "-", client.creation_date, "-", client.last_update, "-", client.sales_person)
    
    def get_client_id(self):
        choice = self.input.input_in_array_of_int("Entrer l'id du client concerné : ")
        return choice
    #pourquoi les or?
    def update_client(self, client):
        print("Taper Entrée pour conserver la valeur sans modification")
        first_and_last_name = self.input.check_string(f"Nom et prénom ({client.first_and_last_name}) : ") or client.first_and_last_name
        email = input(f"Email ({client.email}) : ") or client.email
        phone_number = self.input.check_int(f"Numéro de téléphone ({client.phone_number}) : ") or client.phone_number
        company_name = self.input.check_string(f"Nom de l'entreprise ({client.company_name}) : ") or client.company_name
        creation_date = self.input.check_date(f"Date de création ({client.creation_date}) : ") or client.creation_date
        last_update = self.input.check_date(f"Dernière mise à jour ({client.last_update}) : ") or client.last_update
        sales_person = self.input.check_string(f"Nom du commercial ({client.sales_person}) : ") or client.sales_person
        return first_and_last_name, email, phone_number, company_name, creation_date, last_update, sales_person