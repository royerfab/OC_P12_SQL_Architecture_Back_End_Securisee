from models.config import session
from models.models import Contract, Client
from views.contracts import ContractView
from utils.decorators import login_required, manager_required, sales_required, sales_or_manager_required
from .authentication import AuthenticationController


class ContractController:
    def __init__(self):
        self.contract_view = ContractView()
        self.auth_controller = AuthenticationController()

    # Ici on récupère l'id du sales_contact du client en demandant d'abord l'id du client'
    @login_required
    @manager_required
    def create_contract(self):
        (
            total_amount,
            remaining_amount,
            status,
            client_id,
        ) = self.contract_view.get_contract_data()

        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            sales_contact_id = client.sales_contact_id

            new_contract = Contract(
                client_id=client_id,
                sales_contact_id=sales_contact_id,
                total_amount=total_amount,
                remaining_amount=remaining_amount,
                status=status,
            )
            session.add(new_contract)
            session.commit()
        else:
            print("Client inexistant.")

    @login_required
    def display_contracts(self):
        contracts = session.query(Contract).all()
        self.contract_view.display_contracts(contracts)

    #Affiche les contrats d'un commercial, si c'est celui qui est connecté (avec is_sales_person).
    @login_required
    @sales_or_manager_required
    def display_my_contracts(self):
        sales_contact = self.auth_controller.is_sales_person()
        contracts = session.query(Contract)
        if sales_contact:
            contracts = contracts.filter_by(sales_contact_id=sales_contact.id).all()
        else:
            contracts = contracts.all()
        if contracts:
            self.contract_view.display_contracts(contracts)
            return contracts
        else:
            return None

    @login_required
    @sales_or_manager_required
    def update_contract(self):
        contracts = self.display_my_contracts()
        if contracts:
            contract_id_list = [contract.id for contract in contracts]
            contract_id = self.contract_view.get_contract_id(contract_id_list)
            contract = session.query(Contract).filter_by(id=contract_id).first()
            (
                total_amount,
                remaining_amount,
                status,
            ) = self.contract_view.update_contract(contract)
            contract.total_amount = total_amount
            contract.remaining_amount = remaining_amount
            contract.status = status
            print(contract.status)
            session.commit()
        else:
            print("Vous n'avez pas de contrat.")

    @login_required
    @manager_required
    def delete_contract(self):
        self.display_contracts()
        contract_id = self.contract_view.get_contract_id()
        contract = session.query(Contract).filter_by(id = contract_id).first()
        session.delete(contract)
        session.commit()
            