from .errorview import InputCheckView


class ContractView:
    def __init__(self):
        self.input = InputCheckView()

    def get_contract_data(self):
        client_id = self.input.check_int("Entrer l'id du client associé au contrat : ")
        client_informations = self.input.check_string("Entrer les informations sur le client : ")
        sales_person = self.input.check_string("Entrer le nom du commercial associé au contrat : ")
        total_amount = self.input.check_int("Entrer le montant total du contrat : ")
        remaining_amount = self.input.check_int("Entrer le montant restant à payer : ")
        creation_date = self.input.check_date("Entrer la date de création du contrat : ")
        status = self.input.check_string("Entrer le statut du contrat : ")
        return client_id, client_informations, sales_person, total_amount, remaining_amount, creation_date, status
    
    def display_contracts(self, contracts):
        for contract in contracts:
            print("Contract ID:", contract.id)
            print("Client ID:", contract.client_id)
            print("Client Informations:", contract.client_informations)
            print("Sales Person:", contract.sales_person)
            print("Total Amount:", contract.total_amount)
            print("Remaining Amount:", contract.remaining_amount)
            print("Creation Date:", contract.creation_date)
            print("Status:", contract.status)
            print("---------------------------------------")
    
    def get_contract_id(self):
        choice = self.input.input_in_array_of_int("Entrer l'id du contrat concerné : ")
        return choice
    #pourquoi les or?
    def update_contract(self, contract):
        print("Taper Entrée pour conserver la valeur sans modification")
        client_id = self.input.check_int(f"Client ID ({contract.client_id}) : ") or contract.client_id
        client_informations = self.input.check_string(f"Client Informations ({contract.client_informations}) : ") or contract.client_informations
        sales_person = self.input.check_string(f"Sales Person ({contract.sales_person}) : ") or contract.sales_person
        total_amount = self.input.check_int(f"Total Amount ({contract.total_amount}) : ") or contract.total_amount
        remaining_amount = self.input.check_int(f"Remaining Amount ({contract.remaining_amount}) : ") or contract.remaining_amount
        creation_date = self.input.check_date(f"Creation Date ({contract.creation_date}) : ") or contract.creation_date
        status = self.input.check_string(f"Status ({contract.status}) : ") or contract.status
        return client_id, client_informations, sales_person, total_amount, remaining_amount, creation_date, status
