from tests.pages.vendas.vendas_page import VendasPage

def test_register_sale(webdriver):
    object_sale = VendasPage(webdriver)
    object_sale.open()
    object_sale.click_the_sales_link_button()
    object_sale.register_vendas_button()
    object_sale.select_employee()
    object_sale.select_product()
    object_sale.send_product_registration()
    result = object_sale.sale_registration_title()
    expected = True
    assert result == expected


def test_refresh_button_product(webdriver):
    object_sale = VendasPage(webdriver)
    object_sale.open()
    object_sale.click_the_sales_link_button()
    object_sale.click_refresh_button()
    object_sale.select_product()
    object_sale.submit_change()
    result = object_sale.get_list_of_product()
    expected = 'Lista de Vendas Registradas'
    assert result == expected
