from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "http://localhost:8000"

    def __init__(self, driver):
        self.driver = driver
        self.home = (
            By.XPATH,
            '//*[@class="nav-link" and contains(text(), "Página Inicial")]',
        )
        self.funcionario = (
            By.XPATH,
            '//*[@class="nav-link" and contains(text(), "Funcionários")]',
        )
        self.produto = (
            By.XPATH,
            '//*[@class="nav-link" and contains(text(), "Produtos")]',
        )
        self.venda = (By.XPATH,
                      '//*[@class="nav-link" and contains(text(), "Vendas")]')
        self.employee_link_button = (
            By.XPATH,
            '//a[@class="nav-link" and contains(@href, "/funcionarios/lista")]'
        )
        self.product_link_button = (
            By.XPATH,
            '//a[@class="nav-link" and contains(@href, "/produtos/lista")]'
        )
        self.sales_link_button = (
            By.XPATH,
            '//a[@class="nav-link" and contains(@href, "/vendas/lista")]'
        )

    def open(self):
        self.driver.get(self.URL)

    def get_heading_home_text(self):
        return self.driver.find_element(*self.home).text

    def get_heading_funcionario_text(self):
        return self.driver.find_element(*self.funcionario).text

    def get_heading_produto_text(self):
        return self.driver.find_element(*self.produto).text

    def get_heading_venda_text(self):
        return self.driver.find_element(*self.venda).text

    def click_the_employee_link_button(self):
        self.driver.find_element(*self.employee_link_button).click()

    def click_the_product_link_button(self):
        self.driver.find_element(*self.product_link_button).click()

    def click_the_sales_link_button(self):
        self.driver.find_element(*self.sales_link_button).click()

    def get_the_title_of_the_employees_page(self):
        return WebDriverWait(self.driver, 5).until(
            EC.title_is("Lista de Funcionários")
        )

    def get_the_title_of_the_products_page(self):
        return WebDriverWait(self.driver, 5).until(
            EC.title_is("Lista de Produtos")
        )

    def get_the_title_of_the_sales_page(self):
        return WebDriverWait(self.driver, 5).until(
            EC.title_is("Lista de Vendas")
        )
