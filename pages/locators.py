from selenium.webdriver.common.by import By

class Buttons:

    from_location = (By.XPATH, "//input[@role='searchbox' and @aria-controls='pr_id_1_list']")
    to_location = (By.XPATH, "//input[@role='searchbox' and @aria-controls='pr_id_2_list']")
    select_calendar = (By.XPATH, "//input[contains(@class, 'ng-tns-c58-10')]")
    select_date = (By.XPATH, "//tbody//tr//td//a[contains(@class, 'ui-state-default') and text()='5']")
    first_option_from = (By.XPATH, "//ul[@id='pr_id_1_list']//li[2]")
    first_option_to = (By.XPATH, "//ul[@id='pr_id_2_list']//li[1]")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    wait_for_result = (By.XPATH, "//div[@class='tbis-div']")
    train_headings = (By.XPATH, "//div[contains(@class, 'train-heading')]//strong")
