from framework.utils.logger import Logger
from framework.browser.browser import Browser

from tests.config.oauth import OAuth
from tests.config.urls import Urls
from tests.config.gmail import Gmail
from tests.pages.google_oauth_page import GoogleOAuthPage
from tests.pages.main_page import MainPage
from tests.pages.newsletters_page import NewslettersPage
from tests.pages.unsubscribe_page import UnsubscribePage
from tests.pages.subscription_confirmation_page import SubscriptionConfirmationPage
from tests.api.oauth_api import OAuthAPI
from tests.api.gmail_api import GmailAPI


class TestEuroNewsGmail:
    def test_euro_news_gmail(self, create_browser):
        Logger.step("Preconditions. Getting the code for a token")
        oauth_api = OAuthAPI()
        auth_uri = oauth_api.generate_uri_from_json()
        Browser().set_url(auth_uri)
        google_oath_page = GoogleOAuthPage()
        google_oath_page.send_email_to_email_sign_in_txt_box(OAuth.EMAIL)
        google_oath_page.click_email_next_bttn()
        google_oath_page.send_password_to_password_sign_in_txt_box(OAuth.PASSWORD)
        google_oath_page.click_password_next_bttn()
        google_oath_page.click_advanced_settings_link()
        google_oath_page.click_app_page_link()
        google_oath_page.click_continue_bttn()
        google_oath_page.wait_for_reload_button_to_appear()
        code_url = Browser().get_current_url()

        Logger.step("Preconditions. Retrieving the code from the url")
        code = oauth_api.get_code_from_uri(code_url)

        Logger.step("Preconditions. Exchanging the received code for a token")
        data_for_token_request = oauth_api.generate_data_for_token_request(code)
        token_data = oauth_api.exchange_code_for_token(data_for_token_request)

        Logger.step("Step 1. Opening main page")
        Browser().set_url(Urls.TEST_STAND_URL)
        main_page = MainPage()
        main_page.close_privacy_pop_up_form()
        assert main_page.is_opened(), "Main Page hasn't opened"

        Logger.step("Step 2. Following the link Newsletters in the header")
        main_page.header_form.click_newsletters_link()
        newsletters_page = NewslettersPage()
        assert newsletters_page.is_opened(), "Newsletters Page hasn't opened"

        Logger.step("Step 3. Choosing a random newsletter subscription plan")
        selected_plan = newsletters_page.select_random_newsletters_subscription_plan()
        newsletters_page.click_selected_newsletters_subscription_plan(selected_plan)
        assert newsletters_page.email_subscription_form.is_opened(), "Email Subscription Form hasn't opened"

        Logger.step("Step 4. Entering email and clicking the submit button")
        gmail_api = GmailAPI()
        emails_before = gmail_api.get_email_list(Urls.UNREAD_EMAILS_FROM_SENDER_PATH,
                                                 token_data.get_field_data(Gmail.ACCESS_TOKEN_FIELD))
        newsletters_page.email_subscription_form.send_email_to_email_txt_box()
        newsletters_page.email_subscription_form.click_submit_bttn()
        emails = gmail_api.send_get_requests_until_email_is_delivered(Urls.UNREAD_EMAILS_FROM_SENDER_PATH,
                                                                    token_data.get_field_data(Gmail.ACCESS_TOKEN_FIELD))
        assert len(emails_before) != len(emails), "The email with confirmation hasn't been delivered"

        Logger.step("Step 5. Following the link received from the letter")
        email_object = gmail_api.get_email_object_from_list_by_index(emails, 0)
        email_id = email_object.get_field_data(Gmail.EMAIL_ID_FIELD)
        specific_email = gmail_api.get_email_by_id(Urls.SPECIFIC_EMAIL_PATH, email_id,
                                                   token_data.get_field_data(Gmail.ACCESS_TOKEN_FIELD))
        encoded_email_data = specific_email.get_field_data(Gmail.PAYLOAD_FIELD)[Gmail.PARTS_FIELD][0][Gmail.BODY_FIELD][
            Gmail.DATA_FIELD]
        link = gmail_api.extract_link_from_email(encoded_email_data)
        Browser().set_url(link)
        subscription_confirmation_page = SubscriptionConfirmationPage()
        assert subscription_confirmation_page.is_opened(), "Subscription Confirmation Page hasn't opened"

        Logger.step("Step 6. Clicking Back to the Site Button")
        subscription_confirmation_page.click_back_to_the_site_bttn()
        assert main_page.is_opened(), "Main Page hasn't opened"

        Logger.step("Step 7. Follow the link Newsletters in the header, "
                    "choosing the same newsletter subscription plan as in the step 3, clicking See preview")
        main_page.header_form.click_newsletters_link()
        newsletters_page.click_see_preview_bttn_of_the_selected_plan(selected_plan)
        preview_name = newsletters_page.get_preview_name()
        Browser().switch_to_frame_by_locator(*newsletters_page.get_frame_loc())
        assert newsletters_page.check_if_preview_opened(preview_name, selected_plan) is True, \
            "The preview of the required plan isn't opened"

        Logger.step("Step 8. Finding the link to unsubscribe from the mailing list, following this link in the browser")
        newsletters_page.click_unsubscribe_link_in_the_frame()
        Browser().switch_new_window()
        unsubscribe_page = UnsubscribePage()
        assert unsubscribe_page.is_opened(), "Unsubscribe Page hasn't opened"

        Logger.step("Step 9. Entering the email, clicking Submit button")
        emails_before = gmail_api.get_email_list(Urls.UNREAD_EMAILS_FROM_SENDER_PATH,
                                                 token_data.get_field_data(Gmail.ACCESS_TOKEN_FIELD))
        unsubscribe_page.send_email_to_email_text_box()
        unsubscribe_page.click_confirm_unsubscription_bttn()
        assert unsubscribe_page.check_unsubscribed_label_appeared(), "You Are Unsubscribed hasn't appeared"

        Logger.step("Step 10. Checking that an email with a message about canceling your subscription hasn't arrived")
        emails = gmail_api.get_email_list(Urls.UNREAD_EMAILS_FROM_SENDER_PATH,
                                          token_data.get_field_data("access_token"))
        assert len(emails_before) == len(emails), \
            "An email with a message about cancellation of your subscription has been sent"
