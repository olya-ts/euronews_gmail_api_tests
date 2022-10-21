from framework.elements.base.base_element import BaseElement


class DropDownList(BaseElement):

    def __init__(self, locator, name):
        super(DropDownList, self).__init__(loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(DropDownList, self).__getitem__(key=key)
        return DropDownList(new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(DropDownList, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return DropDownList(new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "DropDown List"
