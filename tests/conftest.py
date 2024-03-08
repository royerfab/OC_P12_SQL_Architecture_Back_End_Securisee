import pytest
from unittest.mock import Mock, patch


@pytest.fixture
def mock_input():
    with patch('builtins.input', return_value='mocked_input'):
        yield


@pytest.fixture
def capfd_mock():
    mock = Mock()
    with patch('sys.stdout', mock):
        yield mock
