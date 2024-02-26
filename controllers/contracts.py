from models.config import session
from models.models import Contract
from views.contracts import ContractView
from utils.decorators import login_required, manager_required, sales_required


class ContractController:
    def __init__(self):
        self.contract_view = ContractView()

    @login_required
    @manager_required
    def create_contract(self):
        (
            client_id,
            client_informations,
            sales_person,
            total_amount,
            remaining_amount,
            creation_date,
            status,
        ) = self.contract_view.get_contract_data()
        new_contract = Contract(
            client_id=client_id,
            client_informations=client_informations,
            sales_person=sales_person,
            total_amount=total_amount,
            remaining_amount=remaining_amount,
            creation_date=creation_date,
            status=status,
        )
        session.add(new_contract)
        session.commit()

    @login_required
    def display_contracts(self):
        contracts = session.query(Contract).all()
        self.contract_view.display_contracts(contracts)

    @login_required
    @manager_required or @sales_required
    def update_contract(self):
        self.display_contracts()
        contract_id = self.contract_view.get_contract_id()
        contract = session.query(Contract).filter_by(id=contract_id).first()
        (
            client_id,
            client_informations,
            sales_person,
            total_amount,
            remaining_amount,
            creation_date,
            status,
        ) = self.contract_view.update_contract(contract)
        contract.client_id = client_id
        contract.client_informations = client_informations
        contract.sales_person = sales_person
        contract.total_amount = total_amount
        contract.remaining_amount = remaining_amount
        contract.creation_date = creation_date
        contract.status = status
        session.commit()

    @login_required
    @manager_required
    def delete_contract(self):
        self.display_contracts()
        contract_id = self.contract_view.get_contract_id()
        contract = session.query(Contract).filter_by(id = contract_id).first()
        session.delete(contract)
        session.commit()
            