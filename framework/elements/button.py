from framework.elements.base.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, locator, name):
        super(Button, self).__init__(loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(Button, self).__getitem__(key=key)
        return Button(new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(Button, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return Button(new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "Button"
