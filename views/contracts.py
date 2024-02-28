from .errorview import InputCheckView


class ContractView:
    def __init__(self):
        self.input = InputCheckView()

    def get_contract_data(self):
        total_amount = self.input.check_int("Entrer le montant total du contrat : ")
        remaining_amount = self.input.check_int("Entrer le montant restant à payer : ")
        status = self.input.status_option()
        client_id = self.input.check_int("Entrer l'id du client associé au contrat : ")
        return total_amount, remaining_amount, status, client_id
    
    def display_contracts(self, contracts):
        for contract in contracts:
            print("Contract ID:", contract.id)
            print("Client ID:", contract.client)
            print("Sales Person:", contract.sales_contact)
            print("Total Amount:", contract.total_amount)
            print("Remaining Amount:", contract.remaining_amount)
            print("Creation Date:", contract.created_at)
            print("Status:", contract.status)
            print("---------------------------------------")
    
    def get_contract_id(self, contract_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du contrat concerné : ", contract_id_list)
        return choice
    #pourquoi les or?
    def update_contract(self, contract):
        print("Taper Entrée pour conserver la valeur sans modification")
        total_amount = self.input.check_int(f"Total Amount ({contract.total_amount}) : ", updated=True) or contract.total_amount
        remaining_amount = self.input.check_int(f"Remaining Amount ({contract.remaining_amount}) : ", updated=True) or contract.remaining_amount
        status = self.input.status_option()
        return total_amount, remaining_amount, status
