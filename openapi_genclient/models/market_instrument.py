# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: n.v.melnikov@tinkoff.ru
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_genclient.configuration import Configuration


class MarketInstrument(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'figi': 'str',
        'ticker': 'str',
        'isin': 'str',
        'min_price_increment': 'float',
        'lot': 'int',
        'currency': 'Currency',
        'name': 'str'
    }

    attribute_map = {
        'figi': 'figi',
        'ticker': 'ticker',
        'isin': 'isin',
        'min_price_increment': 'minPriceIncrement',
        'lot': 'lot',
        'currency': 'currency',
        'name': 'name'
    }

    def __init__(self, figi=None, ticker=None, isin=None, min_price_increment=None, lot=None, currency=None, name=None, local_vars_configuration=None):  # noqa: E501
        """MarketInstrument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._figi = None
        self._ticker = None
        self._isin = None
        self._min_price_increment = None
        self._lot = None
        self._currency = None
        self._name = None
        self.discriminator = None

        self.figi = figi
        self.ticker = ticker
        if isin is not None:
            self.isin = isin
        if min_price_increment is not None:
            self.min_price_increment = min_price_increment
        self.lot = lot
        if currency is not None:
            self.currency = currency
        self.name = name

    @property
    def figi(self):
        """Gets the figi of this MarketInstrument.  # noqa: E501


        :return: The figi of this MarketInstrument.  # noqa: E501
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this MarketInstrument.


        :param figi: The figi of this MarketInstrument.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and figi is None:  # noqa: E501
            raise ValueError("Invalid value for `figi`, must not be `None`")  # noqa: E501

        self._figi = figi

    @property
    def ticker(self):
        """Gets the ticker of this MarketInstrument.  # noqa: E501


        :return: The ticker of this MarketInstrument.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this MarketInstrument.


        :param ticker: The ticker of this MarketInstrument.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ticker is None:  # noqa: E501
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def isin(self):
        """Gets the isin of this MarketInstrument.  # noqa: E501


        :return: The isin of this MarketInstrument.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this MarketInstrument.


        :param isin: The isin of this MarketInstrument.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this MarketInstrument.  # noqa: E501

        Шаг цены  # noqa: E501

        :return: The min_price_increment of this MarketInstrument.  # noqa: E501
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this MarketInstrument.

        Шаг цены  # noqa: E501

        :param min_price_increment: The min_price_increment of this MarketInstrument.  # noqa: E501
        :type: float
        """

        self._min_price_increment = min_price_increment

    @property
    def lot(self):
        """Gets the lot of this MarketInstrument.  # noqa: E501


        :return: The lot of this MarketInstrument.  # noqa: E501
        :rtype: int
        """
        return self._lot

    @lot.setter
    def lot(self, lot):
        """Sets the lot of this MarketInstrument.


        :param lot: The lot of this MarketInstrument.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and lot is None:  # noqa: E501
            raise ValueError("Invalid value for `lot`, must not be `None`")  # noqa: E501

        self._lot = lot

    @property
    def currency(self):
        """Gets the currency of this MarketInstrument.  # noqa: E501


        :return: The currency of this MarketInstrument.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MarketInstrument.


        :param currency: The currency of this MarketInstrument.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def name(self):
        """Gets the name of this MarketInstrument.  # noqa: E501


        :return: The name of this MarketInstrument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MarketInstrument.


        :param name: The name of this MarketInstrument.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarketInstrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketInstrument):
            return True

        return self.to_dict() != other.to_dict()
