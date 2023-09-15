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

class Sector(object):
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
        'code': 'str',
        'name': 'str',
        'industries': 'list[Industry]'
    }

    attribute_map = {
        'code': 'Code',
        'name': 'Name',
        'industries': 'Industries'
    }

    def __init__(self, code=None, name=None, industries=None):  # noqa: E501
        """Sector - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name = None
        self._industries = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if industries is not None:
            self.industries = industries

    @property
    def code(self):
        """Gets the code of this Sector.  # noqa: E501


        :return: The code of this Sector.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Sector.


        :param code: The code of this Sector.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this Sector.  # noqa: E501


        :return: The name of this Sector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sector.


        :param name: The name of this Sector.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def industries(self):
        """Gets the industries of this Sector.  # noqa: E501


        :return: The industries of this Sector.  # noqa: E501
        :rtype: list[Industry]
        """
        return self._industries

    @industries.setter
    def industries(self, industries):
        """Sets the industries of this Sector.


        :param industries: The industries of this Sector.  # noqa: E501
        :type: list[Industry]
        """

        self._industries = industries

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
        if issubclass(Sector, dict):
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
        if not isinstance(other, Sector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
