from src.pages.SaucedemoLoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

def test_login_page_load(webdriver_int):
    LoginPage(webdriver_int).go_to_site()
    assert webdriver_int.title == "Swag Labs"


def test_username_field_is_present(webdriver_int):
    LoginPage(webdriver_int).search_username_fild()


def test_username_field_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_username_field()


def test_username_input(webdriver_int):
    LoginPage(webdriver_int).enter_username(value="standard_user")


def test_passwd_field_is_present(webdriver_int):
    LoginPage(webdriver_int).search_passwd_field()


def test_passwd_field_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_passwd_field()


def test_passwd_input(webdriver_int):
    LoginPage(webdriver_int).enter_passwd(value="secret_sauce")


def test_submit_button(webdriver_int):
    LoginPage(webdriver_int).search_submit_button()


def test_submit_button_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_submit_button()


# This works, but:
# 1) I will have to repeatedly fill in the Username and Password fields for different test cases.
# 2) She looks terrible!
# I think it's worth using pytest.fixture with [username] and [passwd] parameters.
# def test_error_message_is_present(webdriver_int):
#     LoginPage(webdriver_int).go_to_site()
#     action = ActionChains(webdriver_int)
#     username = LoginPage(webdriver_int).click_on_username_field()
#     passwd = LoginPage(webdriver_int).click_on_passwd_field()
#     submit = LoginPage(webdriver_int).search_submit_button()
#     action.send_keys_to_element(username,"qwerty")
#     action.send_keys_to_element(passwd,"123456")
#     action.click(submit)
#     action.perform()
#     LoginPage(webdriver_int).search_error_message_field()





