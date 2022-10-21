from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.button import Button
from framework.utils.logger import Logger
from tests.pages.forms.header_form import HeaderForm


class MainPage(BaseForm):
    header_form = HeaderForm()

    __search_condition = By.XPATH

    __featured_label_loc = "//*[contains(text(), 'Featured')]"

    __agree_and_close_bttn = Button(
        locator=(__search_condition, "//span[text()='Agree and close']"),
        name="Agree and Close Button"
    )

    def __init__(self):
        super().__init__(locator=(MainPage.__search_condition, MainPage.__featured_label_loc),
                         page_name=self.__class__.__name__)

    def close_privacy_pop_up_form(self):
        Logger.info("Waiting for the privacy form to pop up on the " + self.__class__.__name__)
        self.__agree_and_close_bttn.wait_for_is_visible()
        Logger.info("Clicking the Agree and Close button to close the form on the " + self.__class__.__name__)
        self.__agree_and_close_bttn.click()
