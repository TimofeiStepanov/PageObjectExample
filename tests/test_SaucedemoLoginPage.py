import pytest
from src.pages.SaucedemoLoginPage import LoginPage

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

# @pytest.fixture()
# def credentials():
User = ""
Pass = ""


@pytest.fixture()
def valid_credentials():
    global User
    global Pass
    User = "standard_user"
    Pass = "secret_sauce"


@pytest.fixture()
def locked_out_user():
    global User
    global Pass
    User = "locked_out_user"
    Pass = "secret_sauce"


@pytest.fixture()
def problem_user():
    global User
    global Pass
    User = "problem_user"
    Pass = "secret_sauce"


@pytest.fixture()
def performance_glitch_user():
    global User
    global Pass
    User = "performance_glitch_user"
    Pass = "secret_sauce"


@pytest.fixture()
def user_name_not_set():
    global User
    global Pass
    User = ""
    Pass = "secret_sauce"


@pytest.fixture()
def password_not_set():
    global User
    global Pass
    User = "standard_user"
    Pass = ""


@pytest.fixture()
def username_and_password_not_set():
    global User
    global Pass
    User = ""
    Pass = ""


@pytest.fixture()
def username_not_valid():
    global User
    global Pass
    User = "qwerty"
    Pass = "secret_sauce"


@pytest.fixture()
def password_not_valid():
    global User
    global Pass
    User = "standard_user"
    Pass = "123456"


@pytest.fixture()
def username_and_password_not_valid():
    global User
    global Pass
    User = "qwerty"
    Pass = "123456"


@pytest.fixture()
def input_credentials(webdriver_int):
    LoginPage(webdriver_int).go_to_site()
    LoginPage(webdriver_int).enter_username(value=User)
    LoginPage(webdriver_int).enter_passwd(value=Pass)
    LoginPage(webdriver_int).click_on_submit_button()


def test_valid_creds_login(webdriver_int, valid_credentials, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


def test_error_message_is_present(webdriver_int, locked_out_user, input_credentials):
    LoginPage(webdriver_int).search_error_message_field()


def test_locked_out_user_login_message(webdriver_int, locked_out_user, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Sorry, this user has been locked out."


def test_problem_user_login(webdriver_int, problem_user, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


def test_performance_glitch_user_login(webdriver_int, performance_glitch_user, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


def test_user_name_not_set_login(webdriver_int, user_name_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Username is required"


def test_password_not_set_login(webdriver_int, password_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Password is required"


def test_username_and_password_not_set_login(webdriver_int, username_and_password_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Username is required"


def test_username_not_valid_set_login(webdriver_int, username_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Username and password do not match any user in this service"


def test_password_not_valid_set_login(webdriver_int, password_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Username and password do not match any user in this service"


def test_username_and_password_not_valid_set_login(webdriver_int, username_and_password_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Username and password do not match any user in this service" \
                                                   ""
