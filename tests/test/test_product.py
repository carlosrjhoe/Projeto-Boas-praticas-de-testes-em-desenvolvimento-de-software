from tests.pages.produtos.produtos_pages import ProdutosPages
from time import sleep

def test_register_employee(webdriver):
    object_product = ProdutosPages(webdriver)
    sleep(1)
    object_product.open()
    sleep(1)
    object_product.click_the_product_link_button()
    sleep(1)
    object_product.register_product_button()
    sleep(1)
    object_product.register_product()
    sleep(3)
    object_product.send_product_registration()
    sleep(3)
