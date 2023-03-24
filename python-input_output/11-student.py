#!/usr/bin/python3
"""class_to_json"""


class Student:
    """Contains student data
    """

    def _init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class_to_json"""

        if attrs is None or type(attrs) != list:
            return self._dict_
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self._dict_
                if elem in self._dict_.keys():
                    temp[elem] = self._dict_[elem]
            return temp

    def reload_from_json(self, json):
        """reload_from_json"""

        for items in json.keys():
            self._dict_[items] = json[items]
