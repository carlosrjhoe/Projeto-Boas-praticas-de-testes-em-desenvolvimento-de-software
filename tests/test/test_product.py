from tests.pages.produtos.produtos_pages import ProdutosPages

def test_register_product(webdriver):
    object_product = ProdutosPages(webdriver)
    object_product.open()
    object_product.click_the_product_link_button()
    object_product.register_product_button()
    object_product.register_product()
    object_product.send_product_registration()
    result = object_product.get_list_of_product()
    expected = 'Lista de Produtos'
    assert result == expected

def test_refresh_button_product(webdriver):
    object_product = ProdutosPages(webdriver)
    object_product.open()
    object_product.click_the_product_link_button()
    object_product.click_refresh_button()
    result = object_product.get_input_name_product()
    expected = object_product.refresh_name_product()
    object_product.submit_change()
    assert result != expected

def test_exclude_product(webdriver):
    object_product = ProdutosPages(webdriver)
    object_product.open()
    object_product.click_the_product_link_button()
    object_product.exclude_product()
    object_product.submit_product_exclusion()
    result = object_product.get_list_of_product()
    expected = 'Lista de Produtos'
    assert result == expected
