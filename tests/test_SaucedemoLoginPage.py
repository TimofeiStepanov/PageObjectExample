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
    LoginPage(webdriver_int).search_passwd_fild()


def test_passwd_field_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_passwd_field()


def test_passwd_input(webdriver_int):
    LoginPage(webdriver_int).enter_passwd(value="secret_sauce")


def test_submit_button(webdriver_int):
    LoginPage(webdriver_int).search_submit_button()


def test_submit_button_is_clickable(webdriver_int):
    LoginPage(webdriver_int).click_on_submit_button()
