import pytest
from .pages.home_page import HomePage


def test_acesso_home_com_sucesso(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_home_text() == 'Página Inicial'

def test_verificar_home_se_aparece_funcionarios(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_funcionario_text() == 'Funcionários'

def test_verificar_home_se_aparece_produtos(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_produto_text() == 'Produtos'

def test_verificar_home_se_aparece_vendas(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_venda_text() == 'Vendas'