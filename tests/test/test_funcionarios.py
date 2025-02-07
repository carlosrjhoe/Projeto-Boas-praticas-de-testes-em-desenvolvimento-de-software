from tests.pages.funcionario.funcionario_page import FuncionarioPage
from time import sleep


def test_register_employee(webdriver):
    funcionario = FuncionarioPage(webdriver)
    funcionario.open()
    funcionario.click_the_employee_link_button()
    funcionario.register_employee()
    funcionario.fill_employee_form()
    funcionario.send_registration()
    result = funcionario.get_list_of_employees()
    expected = "Lista de Funcionários"
    assert result == expected

