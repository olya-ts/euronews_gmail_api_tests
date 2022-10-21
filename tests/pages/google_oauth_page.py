from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from framework.elements.link import Link
from framework.utils.logger import Logger
from tests.config.oauth import OAuth


class GoogleOAuthPage(BaseForm):
    __search_condition = By.XPATH

    __sign_in_label_loc = "//div[text()='Sign in with Google']"

    __sign_in_input_base_loc = "//input[@type='{name}']"

    __next_bttn_base_loc = "//div[@id='{name}']"

    __email_sign_in_txt_box = TextBox(
            locator=(__search_condition, __sign_in_input_base_loc.format(name="email")),
            name="Email Sign in Text Box"
        )

    __password_sign_in_txt_box = TextBox(
            locator=(__search_condition, __sign_in_input_base_loc.format(name="password")),
            name="Email Sign in Text Box"
        )

    __email_next_bttn = Button(
        locator=(__search_condition, __next_bttn_base_loc.format(name="identifierNext")),
        name="Email Next Button"
    )

    __password_next_bttn = Button(
        locator=(__search_condition, __next_bttn_base_loc.format(name="passwordNext")),
        name="Password Next Button"
    )

    __advanced_settings_link = Link(
        locator=(__search_condition, "//div[@role='button']//preceding-sibling::a"),
        name="Advanced Settings Link"
    )

    __link_to_app_page = Link(
        locator=(__search_condition, f"//a[contains(text(), '{OAuth.APP_NAME}')]"),
        name="Link to the Task's Page"
    )

    __continue_bttn = Button(
        locator=(__search_condition, __next_bttn_base_loc.format(name="submit_approve_access")),
        name="Continue Button"
    )

    __reload_bttn = Button(
        locator=(__search_condition, "//button[@id='reload-button']"),
        name="Reload Button"
    )

    def __init__(self):
        super().__init__(locator=(GoogleOAuthPage.__search_condition, GoogleOAuthPage.__sign_in_label_loc),
                         page_name=self.__class__.__name__)

    def send_email_to_email_sign_in_txt_box(self, email: str):
        Logger.info("Sending email " + email + " to the Email Sign in Text Box on the " + self.__class__.__name__)
        self.__email_sign_in_txt_box.send_keys(email)

    def send_password_to_password_sign_in_txt_box(self, password: str):
        Logger.info("Waiting for the Password Sign in Text Box to be visible on the " + self.__class__.__name__)
        self.__password_sign_in_txt_box.wait_for_is_visible()
        Logger.info("Sending password " + password + " to the Password Sign in Text Box on the "
                    + self.__class__.__name__)
        self.__password_sign_in_txt_box.send_keys(password)

    def click_email_next_bttn(self):
        Logger.info("Clicking Email Next Button on the " + self.__class__.__name__)
        self.__email_next_bttn.click()

    def click_password_next_bttn(self):
        Logger.info("Clicking Password Next Button on the " + self.__class__.__name__)
        self.__password_next_bttn.click()

    def click_advanced_settings_link(self):
        Logger.info("Clicking Advanced Settings Link on the " + self.__class__.__name__)
        self.__advanced_settings_link.click()

    def click_app_page_link(self):
        Logger.info("Clicking Link to Task's Page on the " + self.__class__.__name__)
        self.__link_to_app_page.click()

    def click_continue_bttn(self):
        Logger.info("Waiting for the Continue Button to be visible on the " + self.__class__.__name__)
        self.__continue_bttn.wait_for_is_visible()
        Logger.info("Clicking Continue Button to submit approval of access on the " + self.__class__.__name__)
        self.__continue_bttn.click()

    def wait_for_reload_button_to_appear(self):
        Logger.info("Waiting for Reload Button to be visible on the " + self.__class__.__name__)
        self.__reload_bttn.wait_for_is_visible()
