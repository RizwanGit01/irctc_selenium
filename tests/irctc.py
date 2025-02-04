from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.tests import DemoTest
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException
import time



@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.close()

def test_search_results(driver):    
    driver.get("https://www.irctc.co.in/nget/train-search")
    demo_test = DemoTest(driver)
    demo_test.enter_from_text()
    demo_test.select_first_option_from()
    demo_test.enter_to_text()
    demo_test.select_first_option_to()
    demo_test.select_calendar()
    demo_test.select_date()
    demo_test.search_button()
    demo_test.wait_for_results()
    demo_test.get_train_results()
