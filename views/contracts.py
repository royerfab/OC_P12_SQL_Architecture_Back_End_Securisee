from .errorview import InputCheckView
from rich.console import Console
from rich.table import Table


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
        table = Table(title = "Liste des contrats")
        table.add_column("Contrat id")
        table.add_column("Client")
        table.add_column("Sales contact")
        table.add_column("Total amount")
        table.add_column("Remaining amount")
        table.add_column("Created at")
        table.add_column("Status")
      
        for contract in contracts:
            status = "✅" if contract.status else "❌"
            table.add_row(str(contract.id), str(contract.client), str(contract.sales_contact), str(contract.total_amount),
                          str(contract.remaining_amount), str(contract.created_at), status)

        console = Console()
        console.print(table)
    
    def get_contract_id(self, contract_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du contrat concerné : ", contract_id_list)
        return choice

    def update_contract(self, contract):
        print("Taper Entrée pour conserver la valeur sans modification")
        total_amount = self.input.check_int(f"Total Amount ({contract.total_amount}) : ", updated=True) or contract.total_amount
        remaining_amount = input(f"Remaining Amount ({contract.remaining_amount}) : ")
        status = self.input.status_option()
        return total_amount, remaining_amount, status
    
