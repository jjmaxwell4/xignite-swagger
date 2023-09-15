# coding: utf-8

"""
    XigniteFactSetFundamentals

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Item(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'level': 'str',
        'value': 'str',
        'order': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'level': 'Level',
        'value': 'Value',
        'order': 'Order',
        'unit': 'Unit'
    }

    def __init__(self, type=None, level=None, value=None, order=None, unit=None):  # noqa: E501
        """Item - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._level = None
        self._value = None
        self._order = None
        self._unit = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if level is not None:
            self.level = level
        if value is not None:
            self.value = value
        if order is not None:
            self.order = order
        if unit is not None:
            self.unit = unit

    @property
    def type(self):
        """Gets the type of this Item.  # noqa: E501


        :return: The type of this Item.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Item.


        :param type: The type of this Item.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def level(self):
        """Gets the level of this Item.  # noqa: E501


        :return: The level of this Item.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Item.


        :param level: The level of this Item.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def value(self):
        """Gets the value of this Item.  # noqa: E501


        :return: The value of this Item.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Item.


        :param value: The value of this Item.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def order(self):
        """Gets the order of this Item.  # noqa: E501


        :return: The order of this Item.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Item.


        :param order: The order of this Item.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def unit(self):
        """Gets the unit of this Item.  # noqa: E501


        :return: The unit of this Item.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Item.


        :param unit: The unit of this Item.  # noqa: E501
        :type: str
        """

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Item, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other