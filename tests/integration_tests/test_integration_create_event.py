from unittest.mock import patch
from controllers.clients import ClientController
from controllers.contracts import ContractController
from controllers.events import EventController
from controllers.authentication import AuthenticationController


def test_create_event():
    # Connexion avec un commercial.
    with patch('builtins.input', side_effect=['sales2', 'password']):
        auth_controller = AuthenticationController()
        auth_controller.logout()
        auth_controller.login()
        user = auth_controller.get_current_user()
        assert user is not None
        assert auth_controller.is_sales_person() is not None
        assert auth_controller.is_support() is None
        assert auth_controller.is_manager() is None
        assert auth_controller.is_sales_or_manager() is not None

    # Création d'un client.
    with patch('builtins.input', side_effect=['testcreateclient', 'email@gmail.com', '0000', 'company']):
        client_controller = ClientController()
        client = client_controller.create_client()
        assert client is not None

        # Connexion avec un manager.
        with patch('builtins.input', side_effect=['manager1', 'password']):
            auth_controller = AuthenticationController()
            auth_controller.logout()
            auth_controller.login()
            user = auth_controller.get_current_user()
            assert user is not None

        # Création d'un contrat.
        with patch('builtins.input', side_effect=['1000', '1000', '1', str(client.id)]):
            contract_controller = ContractController()
            contract = contract_controller.create_contract()
            assert contract is not None

        # Connexion avec un commercial.
        with patch('builtins.input', side_effect=['sales2', 'password']):
            auth_controller = AuthenticationController()
            auth_controller.logout()
            auth_controller.login()
            user = auth_controller.get_current_user()
            assert user is not None

        # Création d'un événement.
        with patch('builtins.input', side_effect=[str(contract.id), 'testcreateevent', '2000-01-01',
                                                  '2000-01-01', 'location', '50', 'notes']):
            event_controller = EventController()
            event = event_controller.create_event()
            assert event is not None

        # Connexion avec un manager.
        with patch('builtins.input', side_effect=['manager1', 'password']):
            auth_controller = AuthenticationController()
            auth_controller.logout()
            auth_controller.login()
            user = auth_controller.get_current_user()
            assert user is not None

        # Suppression de l'événement.
        with patch('builtins.input', side_effect=[str(event.id)]):
            event_controller.delete_event()

        # Suppression du contrat.
        with patch('builtins.input', side_effect=[str(contract.id)]):
            contract_controller.delete_contract()

        # Suppression du client.
        with patch('builtins.input', side_effect=[str(client.id)]):
            client_controller.delete_client()
