from framework.elements.base.base_element import BaseElement


class CheckBox(BaseElement):

    def __init__(self, locator, name):
        super(CheckBox, self).__init__(loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(CheckBox, self).__getitem__(key=key)
        return CheckBox(new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(CheckBox, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return CheckBox(new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "Check Box"
