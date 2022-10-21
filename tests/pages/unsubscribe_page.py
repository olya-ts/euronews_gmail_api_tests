from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from framework.elements.label import Label
from framework.utils.logger import Logger
from tests.config.oauth import OAuth


class UnsubscribePage(BaseForm):

    __search_condition = By.XPATH

    __confirm_unsubscription_bttn_loc = "//button[@type='submit']"

    __email_txt_box = TextBox(
        locator=(__search_condition, "//input[@id='email']"),
        name="Email Text Box"
    )

    __confirm_unsubscription_bttn = Button(
        locator=(__search_condition, __confirm_unsubscription_bttn_loc),
        name="Confirm Unsubscription Button"
    )

    __unsubscribed_label = Label(
        locator=(__search_condition, "//p[not(contains(@class, 'text-danger'))]//child::strong"),
        name="You Are Unsubscribed Label"
    )

    def __init__(self):
        super().__init__(locator=(UnsubscribePage.__search_condition,
                                  UnsubscribePage.__confirm_unsubscription_bttn_loc),
                         page_name=self.__class__.__name__)

    def send_email_to_email_text_box(self):
        Logger.info("Sending the email " + OAuth.EMAIL + "to the Email Text Box on the " + self.__class__.__name__)
        self.__email_txt_box.clear_field()
        self.__email_txt_box.send_keys(OAuth.EMAIL)

    def click_confirm_unsubscription_bttn(self):
        Logger.info("Clicking Confirm Unsubscription Button on the " + self.__class__.__name__)
        self.__confirm_unsubscription_bttn.click()

    def check_unsubscribed_label_appeared(self):
        Logger.info("Checking that the Unsubscribed Label has appeared on the " + self.__class__.__name__)
        return self.__unsubscribed_label.is_displayed()
