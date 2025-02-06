from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.home.home_page import HomePage
from faker import Faker
faker = Faker()


class FuncionarioPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nome_input = (By.XPATH, '//input[@id="id_nome"]')
        self.sobrenome_input = (By.XPATH, '//input[@id="id_sobrenome"]')
        self.cpf_input = (By.XPATH, '//input[@id="id_cpf"]')
        self.tempo_de_servico_input = (By.XPATH, '//input[@id="id_tempo_de_servico"]')
        self.remuneracao_input = (By.XPATH, '//input[@id="id_remuneracao"]')
        self.enviar_input = (
            By.XPATH, '//button[@class="btn btn-primary" and contains(text(), "Enviar")]'
        )
        self.cadastrar_funcionario_button = (
            By.XPATH, '//a[@class="btn btn-primary btn-sm" and contains(text(), "Cadastrar Funcionário")]'
        )
        self.list_of_employees = (By.XPATH, '//div[@class="card-header"]/b')

    def register_employee(self):
        try:
            self.driver.implicitly_wait(10)

            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                new_height = self.driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height:
                    break

                last_height = new_height

            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.cadastrar_funcionario_button)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.cadastrar_funcionario_button)
            )

            element.click()

        except ElementClickInterceptedException:
            print("O botão 'Cadastrar Funcionário' não apareceu dentro do tempo limite.")

    def get_list_of_employees(self):
        return self.driver.find_element(*self.list_of_employees).text

    def fill_employee_form(self):
        nome = faker.first_name()
        sobrenome = faker.last_name()
        cpf = faker.unique.random_number(digits=11, fix_len=True)
        tempo_servico = faker.random_int(min=1, max=5)
        remuneracao = faker.random_number(digits=5, fix_len=False)
        self.driver.find_element(*self.nome_input).send_keys(nome)
        self.driver.find_element(*self.sobrenome_input).send_keys(sobrenome)
        self.driver.find_element(*self.cpf_input).send_keys(cpf)
        self.driver.find_element(*self.tempo_de_servico_input).send_keys(tempo_servico)
        self.driver.find_element(*self.remuneracao_input).send_keys(remuneracao)

    def send_registration(self):
        self.driver.find_element(*self.enviar_input).click()
