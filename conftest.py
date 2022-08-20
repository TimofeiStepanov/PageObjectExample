import pytest
import urllib3
from urllib3 import exceptions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Setup commandline parameter for select browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="select browser",
        choices=("firefox", "edge", "chrome")
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

# Setup webdriver for different browsers
@pytest.fixture(scope="session")
def webdriver_int(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, path=r".\\..\\res\\Drivers").install()))

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(path=r".\\..\\res\\Drivers").install()))

    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(path=r".\\..\\res\\Drivers").install()))

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Added marks for tests
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoky:"
    )
    config.addinivalue_line(
        "markers", "functional:"
    )