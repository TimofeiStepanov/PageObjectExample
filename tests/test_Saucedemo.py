from src.pages.SaucedemoStartPage import LoginPage
from src.locators.SaucedemoLocators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


# class test_Login_Page(LoginPage):

def test_login_pade_load(webdriver_int):
    login_page = LoginPage(webdriver_int)
    login_page.go_to_site()


def test_username_field(webdriver_int):
    login_page = LoginPage(webdriver_int)
    login_page.search_username_fild()
    login_page.click_on_username_field()
    login_page.enter_username(value="standard_user")

def test_passwd_field(webdriver_int):
    login_page = LoginPage(webdriver_int)
    login_page.search_passwd_fild()
    login_page.click_on_passwd_field()
    login_page.enter_passwd(value="secret_sauce")

def test_submit_button(webdriver_int):
    login_page = LoginPage(webdriver_int)
    login_page.search_submit_dutton()
    login_page.click_on_submit_button()

# def test_login_form(webdriver_int):
#     actions = ActionChains(webdriver_int)
#     username = LoginPage.enter_username(value="standard_user")
#     passwd = LoginPage.enter_passwd(value="secret_sauce")
#     button_submit = LoginPage.click_on_submit_button
#     actions(username)
#     actions(passwd)
#     actions(button_submit)
#     actions.perform()





