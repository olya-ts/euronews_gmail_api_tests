from framework.elements.base.base_element import BaseElement
from framework.utils.logger import Logger


class Link(BaseElement):

    def __init__(self, locator, name):
        super(Link, self).__init__(loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(Link, self).__getitem__(key=key)
        return Link(new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(Link, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return Link(new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "Link"

    def get_href(self):
        Logger.info("Getting link from the element")
        return super(Link, self).get_attribute("href")
