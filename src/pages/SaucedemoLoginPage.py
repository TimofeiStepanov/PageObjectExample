from src.locators.SaucedemoLocators import Locators
from src.pages.BasePage import BasePage


class LoginPage(BasePage, Locators):

    def search_username_fild(self):
        return self.find_element(Locators.username_field_locator)

    def click_on_username_field(self):
        return self.search_username_fild().click()

    def enter_username(self, value):
        return self.search_username_fild().send_keys(value)

    def search_passwd_field(self):
        return self.find_element(Locators.passwd_field_locator)

    def click_on_passwd_field(self):
        return self.search_passwd_field().click()

    def enter_passwd(self, value):
        return self.search_passwd_field().send_keys(value)

    def search_submit_button(self):
        return self.find_element(Locators.submit_butt_locator)

    def click_on_submit_button(self):
        return self.search_submit_button().click()

    def search_error_message_field(self):
        return self.find_element(Locators.error_message_locator)

    def get_error_message_text(self):
        return self.find_element(Locators.error_message_text_locator).text
