from selenium.webdriver.common.by import By

class HomePage:
    URL = "http://localhost:8000"

    def __init__(self, driver):
        self.driver = driver
        self.home = (By.XPATH, '//*[@class="nav-link" and contains(text(), "Página Inicial")]')

    def open(self):
        self.driver.get(self.URL)

    def get_heading_text(self):
        return self.driver.find_element(*self.home).text
