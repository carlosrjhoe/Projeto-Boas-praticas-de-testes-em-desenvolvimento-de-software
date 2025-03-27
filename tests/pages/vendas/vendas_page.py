from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from tests.pages.home.home_page import HomePage
from tests.pages.produtos.produtos_pages import ProdutosPages
import random

class VendasPage(ProdutosPages):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.register_sale = (
            By.XPATH, '//a[@class="btn btn-primary btn-sm" '
                      'and contains(text(), "Cadastrar Venda")]')
        self.select_employee_button = (By.ID, 'id_funcionario')
        self.select_product_button = (By.ID, 'id_produto')
        self.title_sale = (
            By.XPATH, '//*[@class="card-title" '
                      'and contains(text(), "Cadastro de Venda")]')

    def register_vendas_button(self):
        self.driver.find_element(*self.register_sale).click()

    def select_employee(self):
        element = self.driver.find_element(*self.select_employee_button)
        select = Select(element)
        options = select.options[1:]
        random_choice = random.choice(options)
        select.select_by_value(random_choice.get_attribute("value"))

    def select_product(self):
        element = self.driver.find_element(*self.select_product_button)
        select = Select(element)
        options = select.options[1:]
        random_choice = random.choice(options)
        select.select_by_value(random_choice.get_attribute("value"))

    def sale_registration_title(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.title_sale)
        )
        return element.is_displayed()