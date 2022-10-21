import base64
from bs4 import BeautifulSoup

from framework.utils.logger import Logger


class DecodeUtils:
    @staticmethod
    def decode_base64(encoded_string: str):
        Logger.info("Decoding a base64 string " + encoded_string)
        return base64.urlsafe_b64decode(encoded_string)

    @staticmethod
    def pull_data_from_html(html_data: str):
        Logger.info("Pulling data from HTML")
        return BeautifulSoup(html_data)
