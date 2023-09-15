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

class FundamentalsSet(object):
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
        'as_of_date': 'str',
        'currency': 'str',
        'fundamentals': 'list[Fundamental]'
    }

    attribute_map = {
        'as_of_date': 'AsOfDate',
        'currency': 'Currency',
        'fundamentals': 'Fundamentals'
    }

    def __init__(self, as_of_date=None, currency=None, fundamentals=None):  # noqa: E501
        """FundamentalsSet - a model defined in Swagger"""  # noqa: E501
        self._as_of_date = None
        self._currency = None
        self._fundamentals = None
        self.discriminator = None
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if currency is not None:
            self.currency = currency
        if fundamentals is not None:
            self.fundamentals = fundamentals

    @property
    def as_of_date(self):
        """Gets the as_of_date of this FundamentalsSet.  # noqa: E501


        :return: The as_of_date of this FundamentalsSet.  # noqa: E501
        :rtype: str
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this FundamentalsSet.


        :param as_of_date: The as_of_date of this FundamentalsSet.  # noqa: E501
        :type: str
        """

        self._as_of_date = as_of_date

    @property
    def currency(self):
        """Gets the currency of this FundamentalsSet.  # noqa: E501


        :return: The currency of this FundamentalsSet.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FundamentalsSet.


        :param currency: The currency of this FundamentalsSet.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def fundamentals(self):
        """Gets the fundamentals of this FundamentalsSet.  # noqa: E501


        :return: The fundamentals of this FundamentalsSet.  # noqa: E501
        :rtype: list[Fundamental]
        """
        return self._fundamentals

    @fundamentals.setter
    def fundamentals(self, fundamentals):
        """Sets the fundamentals of this FundamentalsSet.


        :param fundamentals: The fundamentals of this FundamentalsSet.  # noqa: E501
        :type: list[Fundamental]
        """

        self._fundamentals = fundamentals

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
        if issubclass(FundamentalsSet, dict):
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
        if not isinstance(other, FundamentalsSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
