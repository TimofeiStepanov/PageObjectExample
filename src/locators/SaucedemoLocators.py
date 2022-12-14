from selenium.webdriver.common.by import By


class Locators(object):

# Username field
    username_field_locator = (By.ID, "user-name")
# Password field
    passwd_field_locator = (By.ID, "password")
# Submit button
    submit_butt_locator = (By.ID, "login-button")
# Error message
    error_message_locator = (By.XPATH, "//div[contains(@class,'error-message-container error')]")
# Error message text
    error_message_text_locator = (By.XPATH, "//div[contains(@class,'error-message-container error')]//h3")