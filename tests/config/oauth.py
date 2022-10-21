import os


class OAuth(object):
    EXCHANGE_CODE_FOR_TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"

    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
    CLIENT_SECRET_LOCATION = os.path.join(ROOT_DIR, 'tests', "config", "client_secrets.json")

    APP_NAME = ""
    EMAIL = ""
    PASSWORD = ""

    CLIENT_TYPE_FIELD = "web"
    AUTH_URI_FIELD = "auth_uri"
    CLIENT_ID_FIELD = "client_id"
    REDIRECT_URL_FILED = "redirect_uri"
    RESPONSE_TYPE_FIELD = "response_type"
    SCOPE_FIELD = "scope"
    ACCESS_TYPE_FIELD = "access_type"
    CLIENT_SECRET_FIELD = "client_secret"
    CODE_FIELD = "code"
    GRANT_TYPE_FIELD = "grant_type"

    RESPONSE_TYPE_VALUE = "code"
    ACCESS_TYPE_VALUE = "offline"
    SCOPE_VALUE = "https://mail.google.com/"
    GRANT_TYPE_VALUE = "authorization_code"
