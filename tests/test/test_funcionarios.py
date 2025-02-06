from tests.pages.funcionario.funcionario_page import FuncionarioPage
from time import sleep


def test_register_employee(webdriver):
    funcionario = FuncionarioPage(webdriver)
    sleep(1)
    funcionario.open()
    sleep(1)
    funcionario.click_the_employee_link_button()
    sleep(1)
    funcionario.register_employee()
    sleep(1)
    funcionario.fill_employee_form()
    sleep(1)
    funcionario.send_registration()
    sleep(1)
    result = funcionario.get_list_of_employees()
    expected = "Lista de Funcionários"
    assert result == expected

