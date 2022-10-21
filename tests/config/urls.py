class Urls(object):
    TEST_STAND_URL = "https://www.euronews.com/"

    GMAIL_URL = "https://gmail.googleapis.com"
    ALL_EMAILS_PATH = "/gmail/v1/users/{userId}/messages"
    UNREAD_EMAILS_FROM_SENDER_PATH = "/gmail/v1/users/{userId}/messages?q=from:{sender} is:unread"
    SPECIFIC_EMAIL_PATH = "/gmail/v1/users/{userId}/messages/{id}"

    ACCESS_TOKEN_QUERY = "access_token={access_token}"
