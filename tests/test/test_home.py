import pytest
from tests.pages.home.home_page import HomePage
from time import sleep


def test_home_access_success(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_home_text() == "Página Inicial"


def test_verify_home_if_employees_appear(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_funcionario_text() == "Funcionários"


def test_verify_home_if_products_appear(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_produto_text() == "Produtos"


def test_verify_home_if_sales_appear(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    assert home_login.get_heading_venda_text() == "Vendas"

def test_click_the_employee_link_button(webdriver):
    home_login = HomePage(webdriver)
    home_login.open()
    home_login.click_the_employee_link_button()
    assert home_login.get_the_title_of_the_employees_page()
    