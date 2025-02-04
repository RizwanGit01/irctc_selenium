from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import Buttons

class DemoTest:
    def __init__(self, driver: WebDriver):
        self.driver = driver 

    def enter_from_text(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((Buttons.from_location)))
        element.click()
        element.send_keys("Mumbai")

    def enter_to_text(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((Buttons.to_location)))
        element.click()
        element.send_keys("Delhi")
    
    def select_first_option_from(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((Buttons.first_option_from)))
        element.click()

    def select_first_option_to(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((Buttons.first_option_to)))
        element.click()

    def select_calendar(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((Buttons.select_calendar)))
        element.click()

    def select_date(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((Buttons.select_date)))
        element.click()

    def search_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Buttons.search_button)
        )
        element.click()
        
    def wait_for_results(self):
                results = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_all_elements_located(Buttons.wait_for_result)
        )

    def get_train_results(self):
        results = []
        element = self.driver.find_elements(*Buttons.train_headings)
        for i in element:
            results.append(i.text)
        
        with open("results.txt", "w") as f:
                  f.write("\n".join(results))

