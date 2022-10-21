from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.link import Link
from framework.utils.logger import Logger


class HeaderForm(BaseForm):
    __search_condition = By.XPATH

    __search_box_loc = "//div[@id='search-autocomplete']"

    __newsletters_link = Link(
        locator=(__search_condition, "//span[@data-event='newsletter-link-header']"),
        name="Newsletters Link"
    )

    def __init__(self):
        super().__init__(locator=(HeaderForm.__search_condition, HeaderForm.__search_box_loc),
                         page_name=self.__class__.__name__)

    def click_newsletters_link(self):
        Logger.info("Clicking the Newsletters Link on the " + self.__class__.__name__)
        self.__newsletters_link.click()
