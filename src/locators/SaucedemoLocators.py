from selenium.webdriver.common.by import By


class Locators(object):

#Username field
    username_field_locator = (By.ID, "user-name")
# Passuord field
    passwd_field_locator = (By.ID, "password")
# Submit button
    submit_butt_locator = (By.ID, "login-button")