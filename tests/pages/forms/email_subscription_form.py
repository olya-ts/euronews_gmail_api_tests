from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.utils.logger import Logger
from tests.config.oauth import OAuth


class EmailSubscriptionForm(BaseForm):
    __search_condition = By.XPATH

    __submit_bttn_loc = "//input[@value='Submit']"

    __email_text_box = TextBox(
        locator=(__search_condition, "//input[@title='Enter your email']"),
        name="Enter Your Email Text Box"
    )

    __submit_bttn = Button(
        locator=(__search_condition, __submit_bttn_loc),
        name="Submit Button"
    )

    def __init__(self):
        super().__init__(locator=(EmailSubscriptionForm.__search_condition, EmailSubscriptionForm.__submit_bttn_loc),
                         page_name=self.__class__.__name__)

    def send_email_to_email_txt_box(self):
        Logger.info("Sending email " + OAuth.EMAIL + " to the Email Text Box on the " + self.__class__.__name__)
        self.__email_text_box.send_keys(OAuth.EMAIL)

    def click_submit_bttn(self):
        Logger.info("Clicking Submit Button on the " + self.__class__.__name__)
        self.__submit_bttn.js_click()
