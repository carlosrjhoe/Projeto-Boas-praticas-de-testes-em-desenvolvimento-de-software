from tests.pages.funcionario.funcionario_page import FuncionarioPage
from time import sleep

def test_register_employee(webdriver):
    object_employee = FuncionarioPage(webdriver)
    object_employee.open()
    object_employee.click_the_employee_link_button()
    object_employee.register_employee()
    object_employee.fill_employee_form()
    object_employee.send_registration()
    result = object_employee.get_list_of_employees()
    expected = 'Lista de Funcionários'
    assert result == expected

def test_refresh_button_employee(webdriver):
    object_employee = FuncionarioPage(webdriver)
    object_employee.open()
    object_employee.click_the_employee_link_button()
    object_employee.click_refresh_button()
    result = object_employee.get_input_name_employe()
    expected = object_employee.refresh_name_employe()
    object_employee.submit_change()
    assert result != expected

def test_exclude_emplye(webdriver):
    object_employee = FuncionarioPage(webdriver)
    object_employee.open()
    object_employee.click_the_employee_link_button()
    object_employee.exclude_emplye()
    object_employee.submit_employee_exclusion()
    result = object_employee.get_list_of_employees()
    expected = 'Lista de Funcionários'
    assert result == expected

def test_registration_with_invalid_name_field(webdriver):
    object_employee = FuncionarioPage(webdriver)
    object_employee.open()
    object_employee.click_the_employee_link_button()
    object_employee.register_employee()
    object_employee.registration_with_invalid_name_field()
    object_employee.send_registration()
    result = object_employee.submit_fill_in_this_field_nome_input()
    expected = 'Preencha este campo.'
    assert result == expected
