import re

from framework.utils.api.general_api import GeneralAPI
from framework.utils.file_util import FileUtils
from framework.utils.logger import Logger

from tests.config.oauth import OAuth
from tests.models.token import Token


class OAuthAPI(GeneralAPI):
    def __init__(self):
        super().__init__(OAuth.EXCHANGE_CODE_FOR_TOKEN_ENDPOINT)

    @staticmethod
    def generate_uri_from_json():
        Logger.info("Generating uri from the given data")
        data = FileUtils.get_data_from_json(OAuth.CLIENT_SECRET_LOCATION)[OAuth.CLIENT_TYPE_FIELD]
        uri = data[OAuth.AUTH_URI_FIELD] + "?" + OAuth.CLIENT_ID_FIELD + "=" + data[OAuth.CLIENT_ID_FIELD] + \
              "&" + OAuth.REDIRECT_URL_FILED + "=" + data["redirect_uris"][0] + \
              "&" + OAuth.RESPONSE_TYPE_FIELD + "=" + OAuth.RESPONSE_TYPE_VALUE + \
              "&" + OAuth.SCOPE_FIELD + "=" + OAuth.SCOPE_VALUE + \
              "&" + OAuth.ACCESS_TYPE_FIELD + "=" + OAuth.ACCESS_TYPE_VALUE
        return uri

    @staticmethod
    def get_code_from_uri(uri):
        Logger.info("Extracting the code from the uri " + uri)
        return re.search('code=(.+?)&scope', uri).group(1)

    @staticmethod
    def generate_data_for_token_request(code):
        Logger.info("Generating data for the post request to obtain tokens")
        json_data = FileUtils.get_data_from_json(OAuth.CLIENT_SECRET_LOCATION)[OAuth.CLIENT_TYPE_FIELD]
        data = {OAuth.CLIENT_ID_FIELD: json_data[OAuth.CLIENT_ID_FIELD],
                OAuth.CLIENT_SECRET_FIELD: json_data[OAuth.CLIENT_SECRET_FIELD],
                OAuth.CODE_FIELD: code,
                OAuth.GRANT_TYPE_FIELD: OAuth.GRANT_TYPE_VALUE,
                OAuth.REDIRECT_URL_FILED: json_data["redirect_uris"][0]}
        return data

    def exchange_code_for_token(self, data):
        Logger.info("Exchanging the received code for tokens")
        response = self.send_post_request(path="", data=data)
        return Token(**response.json())
