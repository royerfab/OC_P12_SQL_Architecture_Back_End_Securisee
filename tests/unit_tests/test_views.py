from unittest.mock import patch
from views.authentication import AuthenticationView
from views.clients import ClientView
from views.contracts import ContractView
from views.events import EventView
from views.users import UserView
from views.menu import MenuView


def test_authentication_view():
    auth_view = AuthenticationView()

    # Test get_login_data
    with patch('builtins.input', side_effect=['username', 'password']):
        username, password = auth_view.get_login_data()
        assert username == 'username'
        assert password == 'password'


def test_client_view():
    client_view = ClientView()

    # Test get_client_data
    with patch('builtins.input', side_effect=['John Doe', 'john.doe@example.com', '123456789', 'Company Inc']):
        first_and_last_name, email, phone_number, company_name = client_view.get_client_data()
        assert first_and_last_name == 'John Doe'
        assert email == 'john.doe@example.com'
        assert phone_number == '123456789'
        assert company_name == 'Company Inc'


def test_contract_view():
    contract_view = ContractView()

    # Test get_contract_data
    with patch('builtins.input', side_effect=['5000', '2000', '1', '1']):
        total_amount, remaining_amount, status, client_id = contract_view.get_contract_data()
        assert total_amount == 5000
        assert remaining_amount == 2000
        assert status is True
        assert client_id == 1


def test_event_view():
    event_view = EventView()

    # Test get_event_data
    with patch('builtins.input', side_effect=[
            '1', 'Event Test', '2024-02-01', '2024-02-02', 'Location', '100', 'Notes']):
        contract_id, name, event_date_start, event_date_end, location, attendees, notes = event_view.get_event_data()
        assert contract_id == 1
        assert name == 'Event Test'
        assert event_date_start == '2024-02-01'
        assert event_date_end == '2024-02-02'
        assert location == 'Location'
        assert attendees == 100
        assert notes == 'Notes'


def test_user_view():
    user_view = UserView()

    # Test get_user_data
    with patch('builtins.input', side_effect=['JohnDoe', 'password', '1']):
        username, password, role = user_view.get_user_data()
        assert username == 'JohnDoe'
        assert password == 'password'
        assert role == 'gestion'


def test_menu_view():
    menu_view = MenuView()

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.main_menu()
        assert choice == 1

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.user_menu()
        assert choice == 1

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.client_menu()
        assert choice == 1

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.contract_menu()
        assert choice == 1

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.contract_display_menu()
        assert choice == 1

    with patch('builtins.input', side_effect=['1']):
        choice = menu_view.event_menu()
        assert choice == 1
