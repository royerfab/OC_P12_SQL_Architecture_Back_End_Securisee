from unittest.mock import patch
from controllers.authentication import AuthenticationController


def test_authentication_user():
    # Test avec un username et un mot de passe valides
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

        auth_controller.logout()
        user = auth_controller.get_current_user()
        assert user is None
