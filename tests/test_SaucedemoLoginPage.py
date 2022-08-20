import pytest
from src.pages.SaucedemoLoginPage import LoginPage


@pytest.mark.smoky
def test_login_page_load(webdriver_int):
    LoginPage(webdriver_int).go_to_site()
    assert webdriver_int.title == "Swag Labs"


@pytest.mark.smoky
def test_username_field_is_present(webdriver_int):
    LoginPage(webdriver_int).search_username_fild()


@pytest.mark.smoky
def test_username_field_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_username_field()


@pytest.mark.smoky
def test_username_input(webdriver_int):
    LoginPage(webdriver_int).enter_username(value="standard_user")


@pytest.mark.smoky
def test_passwd_field_is_present(webdriver_int):
    LoginPage(webdriver_int).search_passwd_field()


@pytest.mark.smoky
def test_passwd_field_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_passwd_field()


@pytest.mark.smoky
def test_passwd_input(webdriver_int):
    LoginPage(webdriver_int).enter_passwd(value="secret_sauce")


@pytest.mark.smoky
def test_submit_button(webdriver_int):
    LoginPage(webdriver_int).search_submit_button()


@pytest.mark.smoky
def test_submit_button_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_submit_button()


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


@pytest.mark.functional
def test_valid_creds_login(webdriver_int, valid_credentials, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.smoky
@pytest.mark.functional
def test_error_message_is_present(webdriver_int, locked_out_user, input_credentials):
    LoginPage(webdriver_int).search_error_message_field()


@pytest.mark.functional
def test_locked_out_user_login_message(webdriver_int, locked_out_user, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Sorry, this user has been locked out."


@pytest.mark.functional
def test_problem_user_login(webdriver_int, problem_user, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.functional
def test_performance_glitch_user_login(webdriver_int, performance_glitch_user, input_credentials):
    assert webdriver_int.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.functional
def test_user_name_not_set_login(webdriver_int, user_name_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Username is required"


@pytest.mark.functional
def test_password_not_set_login(webdriver_int, password_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Password is required"


@pytest.mark.functional
def test_username_and_password_not_set_login(webdriver_int, username_and_password_not_set, input_credentials):
    assert LoginPage(webdriver_int).get_error_message_text() == "Epic sadface: Username abd password is required"

# The error message should inform about which parameter is set incorrectly.
@pytest.mark.functional
def test_username_not_valid_set_login(webdriver_int, username_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Username do not match any user in this service"

# The error message should inform about which parameter is set incorrectly.
@pytest.mark.functional
def test_password_not_valid_set_login(webdriver_int, password_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Password do not valid for this user"


@pytest.mark.functional
def test_username_and_password_not_valid_set_login(webdriver_int, username_and_password_not_valid, input_credentials):
    assert LoginPage(
        webdriver_int).get_error_message_text() == "Epic sadface: Username and password do not match any user in this service"
