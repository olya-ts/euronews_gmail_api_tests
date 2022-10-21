from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.button import Button
from framework.utils.logger import Logger
from tests.pages.forms.header_form import HeaderForm


class SubscriptionConfirmationPage(BaseForm):
    header_form = HeaderForm()

    __search_condition = By.XPATH

    __subscription_confirmed_label_loc = "//*[text()='Your subscription has been successfully confirmed.']"

    __back_to_the_site_bttn = Button(
        locator=(__search_condition, "//a[@aria-label='Back to the site']"),
        name="Back To The Site Button"
    )

    def __init__(self):
        super().__init__(locator=(SubscriptionConfirmationPage.__search_condition,
                                  SubscriptionConfirmationPage.__subscription_confirmed_label_loc),
                         page_name=self.__class__.__name__)

    def click_back_to_the_site_bttn(self):
        Logger.info("Clicking Back To The Site Button on the " + self.__class__.__name__)
        self.__back_to_the_site_bttn.click()
