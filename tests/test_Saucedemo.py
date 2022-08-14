from src.pages.SaucedemoStartPage import LoginPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



def test_login_pade_load(webdriver_int):
    LoginPage(webdriver_int).go_to_site()


def test_username_field(webdriver_int):
    LoginPage(webdriver_int).search_username_fild()
    LoginPage(webdriver_int).click_on_username_field()
    LoginPage(webdriver_int).enter_username(value="standard_user")

def test_passwd_field(webdriver_int):
    LoginPage(webdriver_int).search_passwd_fild()
    LoginPage(webdriver_int).click_on_passwd_field()
    LoginPage(webdriver_int).enter_passwd(value="secret_sauce")

def test_submit_button(webdriver_int):
    LoginPage(webdriver_int).search_submit_dutton()
    LoginPage(webdriver_int).click_on_submit_button()

# def test_login_form(webdriver_int):
#     actions = ActionChains(webdriver_int)
#     username = LoginPage.enter_username(value="standard_user")
#     passwd = LoginPage.enter_passwd(value="secret_sauce")
#     button_submit = LoginPage.click_on_submit_button
#     actions(username)
#     actions(passwd)
#     actions(button_submit)
#     actions.perform()





