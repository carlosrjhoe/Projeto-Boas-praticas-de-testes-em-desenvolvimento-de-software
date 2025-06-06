from tests.pages.home.home_page import HomePage


def test_home_access_success(webdriver):
    home = HomePage(webdriver)
    home.open()
    result = home.get_heading_home_text()
    expected = "Página Inicial"
    assert result == expected


def test_verify_home_if_employees_appear(webdriver):
    home = HomePage(webdriver)
    home.open()
    result = home.get_heading_funcionario_text()
    expected = "Funcionários"
    assert result == expected


def test_verify_home_if_products_appear(webdriver):
    home = HomePage(webdriver)
    home.open()
    result = home.get_heading_produto_text()
    expected = "Produtos"
    assert result == expected


def test_verify_home_if_sales_appear(webdriver):
    home = HomePage(webdriver)
    home.open()
    result = home.get_heading_venda_text()
    expected = "Vendas"
    assert result == expected


def test_click_the_employee_link_button(webdriver):
    home = HomePage(webdriver)
    home.open()
    home.click_the_employee_link_button()
    result = home.get_the_title_of_the_employees_page()
    expected = True
    assert result == expected


def test_click_the_products_link_button(webdriver):
    home = HomePage(webdriver)
    home.open()
    home.click_the_product_link_button()
    result = home.get_the_title_of_the_products_page()
    expected = True
    assert result == expected


def test_click_the_sales_link_button(webdriver):
    home = HomePage(webdriver)
    home.open()
    home.click_the_sales_link_button()
    result = home.get_the_title_of_the_sales_page()
    expected = True
    assert result == expected
