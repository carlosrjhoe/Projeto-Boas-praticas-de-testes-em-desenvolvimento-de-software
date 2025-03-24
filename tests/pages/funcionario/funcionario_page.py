from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.home.home_page import HomePage
from faker import Faker
faker = Faker('pt_BR')


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
            By.XPATH, '//a[@class="btn btn-primary btn-sm" '
                      'and contains(text(), "Cadastrar Funcionário")]'
        )
        self.list_of_employees = (By.XPATH, '//div[@class="card-header"]/b')
        self.refresh_button = (
            By.XPATH, '//a[@class="btn btn-primary btn-sm" and contains(text(), "Atualizar")]'
        )
        self.input_name_employe = (By.XPATH, '//input[@id="id_nome"]')
        self.exclude_button = (
            By.XPATH, '//a[@class="btn btn-danger btn-sm"][1]'
        )
        self.confirm_employee_exclusion = (
            By.XPATH, '//button[@class="btn btn-danger" '
                      'and contains(text(), "Excluir")]'
        )

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
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.list_of_employees)
        ).text
        return element

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

    def click_refresh_button(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.refresh_button)
        )
        element.click()

    def get_input_name_employe(self):
        element = self.driver.find_element(*self.input_name_employe)
        value = element.get_attribute('value')
        return value

    def refresh_name_employe(self):
        nome = faker.first_name()
        value = self.driver.find_element(*self.nome_input).send_keys(nome)
        return value

    def submit_change(self):
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    def exclude_emplye(self):
        self.driver.find_element(*self.exclude_button).click()

    def submit_employee_exclusion(self):
        self.driver.find_element(*self.confirm_employee_exclusion).click()