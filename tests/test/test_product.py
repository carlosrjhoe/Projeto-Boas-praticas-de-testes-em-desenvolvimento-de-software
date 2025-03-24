from tests.pages.produtos.produtos_pages import ProdutosPages

def test_register_employee(webdriver):
    object_product = ProdutosPages(webdriver)
    object_product.open()
    object_product.click_the_product_link_button()
    object_product.register_product_button()
    object_product.register_product()
    object_product.send_product_registration()
    result = object_product.get_list_of_product()
    expected = 'Lista de Produtos'
    assert result == expected