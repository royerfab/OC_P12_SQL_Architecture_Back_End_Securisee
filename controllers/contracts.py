from models.config import session
from models.models import Contract
from views.contracts import ContractView
from utils.decorators import login_required, manager_required, sales_required, sales_or_manager_required
from .authentication import AuthenticationController


class ContractController:
    def __init__(self):
        self.contract_view = ContractView()
        self.auth_controller = AuthenticationController()

    @login_required
    @manager_required
    def create_contract(self):
        (
            client_id,
            client_informations,
            sales_contact_id,
            sales_contact_info,
            total_amount,
            remaining_amount,
            created_at,
            status,
        ) = self.contract_view.get_contract_data()
        new_contract = Contract(
            client_id=client_id,
            client_informations=client_informations,
            sales_contact_id=sales_contact_id,
            sales_contact_info=sales_contact_info,
            total_amount=total_amount,
            remaining_amount=remaining_amount,
            created_at=created_at,
            status=status,
        )
        session.add(new_contract)
        session.commit()

    @login_required
    def display_contracts(self):
        contracts = session.query(Contract).all()
        self.contract_view.display_contracts(contracts)

    #Affiche les contrats d'un commercial.
    @login_required
    @sales_required
    def display_my_contracts(self):
        current_user = self.auth_controller.get_current_user()
        contracts = session.query(Contract).filter_by(sales_contact_id=current_user.id)
        if contracts.count() >0:
            self.contract_view.display_contracts(contracts)
            return contracts
        else:
            return None

    @login_required
    @sales_or_manager_required
    def update_contract(self):
        contracts = self.display_contracts()
        if contracts:
            contract_id_list = [contract.id for contract in contracts]
            contract_id = self.contract_view.get_contract_id(contract_id_list)
            contract = session.query(Contract).filter_by(id=contract_id).first()
            (
                client_id,
                client_informations,
                sales_contact_id,
                sales_contact_info,
                total_amount,
                remaining_amount,
                created_at,
                status,
            ) = self.contract_view.update_contract(contract)
            contract.client_id = client_id
            contract.client_informations = client_informations
            sales_contact_id = sales_contact_id
            contract.sales_contact_info = sales_contact_info
            contract.total_amount = total_amount
            contract.remaining_amount = remaining_amount
            contract.created_at = created_at
            contract.status = status
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
            