from string import digits

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.home.home_page import HomePage
from faker import Faker



class ProdutosPages(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker('pt_BR')
        self.product_name = (By. ID, 'id_nome')
        self.product_descricao = (By.ID, 'id_descricao')
        self.product_preco = (By.ID, 'id_preco')
        self.enviar_product_input = (
            By.XPATH, '//button[@class="btn btn-primary"'
                      ' and contains(text(), "Enviar")]')
        self.list_of_product = (By.XPATH, '//div[@class="card-header"]/b')

    def register_product_button(self):
        self.driver.find_element(
            By.XPATH, '//a[@class="btn btn-primary btn-sm"'
                      ' and contains(text(), "Cadastrar Produto")]'
        ).click()

    def register_product(self):
        produto = self.faker.word().capitalize() + ' ' +self.faker.word()
        descricao_produto = self.faker.sentence(nb_words=15)
        preco_produto = self.faker.random_number(digits=2, fix_len=True) + 0.99
        self.driver.find_element(*self.product_name).send_keys(produto)
        self.driver.find_element(
            *self.product_descricao).send_keys(descricao_produto)
        self.driver.find_element(
            *self.product_preco).send_keys(str(preco_produto))

    def send_product_registration(self):
        submit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.enviar_product_input)
        )
        # 2. Scroll otimizado com verificação de posição
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});",
            submit
        )

        # 3. Espera adicional após scroll
        WebDriverWait(self.driver, 5).until(
            lambda d: submit.is_displayed() and
                      submit.location_once_scrolled_into_view['y'] <
                      d.execute_script("return window.innerHeight")
        )

        # 4. Clique com verificação de sobreposição
        self.driver.execute_script("arguments[0].click();", submit)

    def get_list_of_product(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.list_of_product)
        ).text
        return element
