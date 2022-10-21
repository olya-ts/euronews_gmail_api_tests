from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.link import Link
from framework.elements.button import Button
from framework.elements.label import Label
from framework.utils.logger import Logger
from framework.utils.random_util import RandomUtils
from tests.pages.forms.email_subscription_form import EmailSubscriptionForm


class NewslettersPage(BaseForm):
    email_subscription_form = EmailSubscriptionForm()

    __search_condition = By.XPATH

    __our_newsletters_heading_loc = "//span[text()='Our newsletters']"

    __newsletters_subscription_plan_base_loc = \
        "//*[text()='{name}']//following::label[contains(text(), 'Select this newsletter')]"

    __see_preview_bttn_base_loc = "//*[text()='{name}']//following::a"

    __subscription_plan_frame_label_base_loc = "//div[@class='modal'][contains(@style, 'display: inline-block')]"

    __frame_loc = __subscription_plan_frame_label_base_loc + "//child::iframe[@class='iframe-preview']"

    __all_newsletters_subscription_plans = Link(
        locator=(__search_condition, "//child::div[@class='p-8']//child::h2[text()]"),
        name="All Newsletters Subscription Plans"
    )

    __unsubscribe_link_in_frame = Link(
        locator=(__search_condition, "//a[contains(text(), 'unsubscribe by clicking here')]"),
        name="Unsubscribe Link in the frame"
    )

    __subscription_plan_frame_label = Label(
        locator=(__search_condition, __subscription_plan_frame_label_base_loc),
        name="Subscription Plan Frame's Label"
    )

    __instructions_to_complete_subscription = Label(
        locator=(__search_condition, "//div[@id='additional-data-modal'][contains(@style, 'display: inline-block')]"),
        name="Instructions to Complete Subscription Label"
    )

    def __init__(self):
        super().__init__(locator=(NewslettersPage.__search_condition, NewslettersPage.__our_newsletters_heading_loc),
                         page_name=self.__class__.__name__)

    def get_newsletters_subsc_plan_list(self):
        Logger.info("Getting a list of Subscription Plans' texts on the " + self.__class__.__name__)
        return self.__all_newsletters_subscription_plans.get_list_of_elems_texts()

    def select_random_newsletters_subscription_plan(self):
        Logger.info("Selecting a random Newsletters Subscription Plan on the " + self.__class__.__name__)
        selected = RandomUtils.select_random_item_from_list(self.get_newsletters_subsc_plan_list())
        Logger.info("Randomly selected Newsletters Subscription Plan is " + selected)
        return selected

    def click_selected_newsletters_subscription_plan(self, selected_plan):
        Logger.info("Clicking on the randomly selected Newsletters Subscription Plan "
                    + selected_plan + " on the " + self.__class__.__name__)
        selected_subscription_plan_link = Link(
            locator=(self.__search_condition,
                     self.__newsletters_subscription_plan_base_loc.format(name=selected_plan)),
            name="Selected Newsletters Subscription Plan")
        selected_subscription_plan_link.click()

    def click_see_preview_bttn_of_the_selected_plan(self, selected_plan):
        Logger.info("Clicking on the See Preview Button of the selected plan "
                    + selected_plan + " on the " + self.__class__.__name__)
        see_preview_bttn = Button(
            locator=(self.__search_condition,
                     self.__see_preview_bttn_base_loc.format(name=selected_plan)),
            name="See Preview Button")
        see_preview_bttn.js_click()

    def click_unsubscribe_link_in_the_frame(self):
        Logger.info("Clicking Unsubscribe Link in the frame " + self.__class__.__name__)
        self.__unsubscribe_link_in_frame.js_click()

    def get_frame_loc(self):
        Logger.info("Getting the loc for the frame on the " + self.__class__.__name__)
        return self.__search_condition, self.__frame_loc

    def get_preview_name(self):
        Logger.info("Waiting for the preview's name to be visible on the " + self.__class__.__name__)
        self.__subscription_plan_frame_label.wait_for_is_visible()
        Logger.info("Getting preview's name  on the " + self.__class__.__name__)
        return self.__subscription_plan_frame_label.get_attribute("id")

    def check_if_preview_opened(self, preview_name: str, selected_plan: str):
        Logger.info("Checking if the preview of " + selected_plan + " has opened on the " + self.__class__.__name__)
        return selected_plan.lower() in preview_name.replace("-", " ")
