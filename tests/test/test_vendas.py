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