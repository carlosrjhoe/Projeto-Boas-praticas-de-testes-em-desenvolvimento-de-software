from selenium.webdriver.common.by import By

class HomePage:
    URL = "http://localhost:8000"

    def __init__(self, driver):
        self.driver = driver
        self.home = (By.XPATH, '//*[@class="nav-link" and contains(text(), "Página Inicial")]')
        self.funcionario = (By.XPATH, '//*[@class="nav-link" and contains(text(), "Funcionários")]')
        self.produto = (By.XPATH, '//*[@class="nav-link" and contains(text(), "Produtos")]')
        self.venda = (By.XPATH, '//*[@class="nav-link" and contains(text(), "Vendas")]')

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