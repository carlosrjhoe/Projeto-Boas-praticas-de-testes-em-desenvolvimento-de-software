import pytest
from .pages.home_page import HomePage


def test_acesso_home_com_sucesso(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_text() == 'Página Inicial'