from framework.utils.api.general_api import GeneralAPI
from framework.utils.logger import Logger
from framework.utils.decode_util import DecodeUtils

from tests.config.urls import Urls
from tests.config.oauth import OAuth
from tests.config.gmail import Gmail
from tests.models.email import Email


class GmailAPI(GeneralAPI):
    def __init__(self):
        super().__init__(Urls.GMAIL_URL)

    def get_email_list(self, path: str, access_token: str):
        Logger.info("Getting a list of emails")
        full_path = path.format(userId=OAuth.EMAIL, sender=Gmail.SENDER) + "&" + Urls.ACCESS_TOKEN_QUERY.format(access_token=access_token)
        response = self.send_get_request(full_path)
        try:
            emails = [Email(**email) for email in response.json()["messages"]]
        except KeyError:
            Logger.warning("The email list is empty")
            emails = ()
        return emails

    def get_email_by_id(self, path: str, email_id: str, access_token: str):
        Logger.info("Getting an email with id " + email_id)
        full_path = path.format(userId=OAuth.EMAIL, id=email_id) + "?" + Urls.ACCESS_TOKEN_QUERY.format(access_token=access_token)
        email = self.send_get_request(full_path)
        return Email(**email.json())

    @staticmethod
    def extract_link_from_email(encoded_data: str):
        html_email_data = DecodeUtils.decode_base64(encoded_data)
        pulled_data = DecodeUtils.pull_data_from_html(html_email_data)
        return pulled_data.find('a').get('href')

    @staticmethod
    def wait_for_email_delivery(emails):
        Logger.info("Checking for the email to be delivered")
        return isinstance(emails, list)

    @staticmethod
    def get_email_object_from_list_by_index(emails, index: int):
        Logger.info("Getting an email object from the list by the index " + str(index))
        try:
            email_object = emails[index]
            return email_object
        except IndexError:
            Logger.error("The index " + str(index) + "is out of range in the given list")

    def send_get_requests_until_email_is_delivered(self, path: str, access_token: str):
        Logger.info("Sending get requests until the email is delivered")
        result = self.get_email_list(path, access_token)
        while self.wait_for_email_delivery(result) is False:
            result = self.get_email_list(path, access_token)
        return result
