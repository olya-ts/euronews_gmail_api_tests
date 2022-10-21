import pytest
from framework.browser.browser import Browser
from tests.config.browser import BrowserConfig


@pytest.fixture(scope="session")
def create_browser(request):
    Browser.get_browser().set_up_driver(browser_key=BrowserConfig.BROWSER)
    Browser.get_browser().maximize(browser_key=BrowserConfig.BROWSER)

    yield

    for browser_key in list(Browser.get_browser().get_driver_names()):
        Browser.get_browser().quit(browser_key=browser_key)
