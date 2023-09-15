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

class CompanyFinancialStatements(object):
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
        'company': 'AllOfCompanyFinancialStatementsCompany',
        'financial_statements': 'list[FinancialStatement]'
    }

    attribute_map = {
        'company': 'Company',
        'financial_statements': 'FinancialStatements'
    }

    def __init__(self, company=None, financial_statements=None):  # noqa: E501
        """CompanyFinancialStatements - a model defined in Swagger"""  # noqa: E501
        self._company = None
        self._financial_statements = None
        self.discriminator = None
        if company is not None:
            self.company = company
        if financial_statements is not None:
            self.financial_statements = financial_statements

    @property
    def company(self):
        """Gets the company of this CompanyFinancialStatements.  # noqa: E501


        :return: The company of this CompanyFinancialStatements.  # noqa: E501
        :rtype: AllOfCompanyFinancialStatementsCompany
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CompanyFinancialStatements.


        :param company: The company of this CompanyFinancialStatements.  # noqa: E501
        :type: AllOfCompanyFinancialStatementsCompany
        """

        self._company = company

    @property
    def financial_statements(self):
        """Gets the financial_statements of this CompanyFinancialStatements.  # noqa: E501


        :return: The financial_statements of this CompanyFinancialStatements.  # noqa: E501
        :rtype: list[FinancialStatement]
        """
        return self._financial_statements

    @financial_statements.setter
    def financial_statements(self, financial_statements):
        """Sets the financial_statements of this CompanyFinancialStatements.


        :param financial_statements: The financial_statements of this CompanyFinancialStatements.  # noqa: E501
        :type: list[FinancialStatement]
        """

        self._financial_statements = financial_statements

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
        if issubclass(CompanyFinancialStatements, dict):
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
        if not isinstance(other, CompanyFinancialStatements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
