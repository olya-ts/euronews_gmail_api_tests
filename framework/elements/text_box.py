from selenium.webdriver.common.keys import Keys

from framework.utils.logger import Logger
from framework.elements.base.base_element import BaseElement


class TextBox(BaseElement):
    def __init__(self, locator, name):
        super(TextBox, self).__init__(loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(TextBox, self).__getitem__(key=key)
        return TextBox(new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(TextBox, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return TextBox(new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "TextBox"

    def clear_field(self):
        Logger.info("Deleting text in the elem " + self.get_name())
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys_without_click(Keys.DELETE)
