import sys
import os

# aqui você precisa ajustar para o caminho absoluto da raiz do seu projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

src_dir = os.path.join(project_root, 'src')
sys.path.insert(0, src_dir)

from unittest.mock import Mock
from capi.src import *

def test_create_user_use_case():
    mock_user_repository = Mock()
    use_case = CreateUserUseCase(mock_user_repository)
    name = "John"
    email = "john@example.com"
    use_case.execute(name, email)
    mock_user_repository.create.assert_called_once_with(User(name=name, email=email))
