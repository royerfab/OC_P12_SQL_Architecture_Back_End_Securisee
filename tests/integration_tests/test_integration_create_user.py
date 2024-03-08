from unittest.mock import patch
from controllers.users import UserController
from controllers.authentication import AuthenticationController


def test_create_user():
    # Test avec un username et un mot de passe valides
    with patch('builtins.input', side_effect=['manager1', 'password']):
        auth_controller = AuthenticationController()
        auth_controller.logout()
        auth_controller.login()
        user = auth_controller.get_current_user()
        assert user is not None
        assert auth_controller.is_sales_person() is None
        assert auth_controller.is_support() is None
        assert auth_controller.is_manager() is not None
        assert auth_controller.is_sales_or_manager() is not None

    with patch('builtins.input', side_effect=['testcreateuser', 'password', '1']):
        user_controller = UserController()
        user = user_controller.create_user()
        assert user is not None
        with patch('builtins.input', side_effect=[str(user.id)]):
            user_controller.delete_user()
