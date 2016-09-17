"""Lightweight API wrapper for
`browser-info.net <http://www.browser-info.net/useragents>`_.
"""

from lxml import html
import urllib


baseUrl = 'http://www.browser-info.net/useragents'
recentXpath = ('(//div[@class="datatable"])[1]//tr/td[2]/a/text()')
popularXpath = ('(//div[@class="datatable"])[2]//tr/td[2]/a/text()')
limit = 20


def _getResults(amount, xPath):
    amount = _sanitizeAmount(amount)
    f = urllib.urlopen(baseUrl)
    tree = html.fromstring(f.read())
    items = tree.xpath(xPath)

    return items[:amount]


def _sanitizeAmount(amount):
    if amount < 0:
        return 0
    if amount > limit:
        return limit

    return amount


def popular(amount=20):
    """Fetches populsr UA strings.

    Retrieves most popular UA strings, up to a maximum of 20.

    :param amount: The amount of UA strings to retrieve
    :type amount: int
    :returns: List of UA strings
    :rtype: list

    :Example:

    >>> import browserinfo
    >>> browserinfo.popular(1)
    ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)']

    """

    return _getResults(amount, popularXpath)


def recent(amount=20):
    """Fetches recent UA strings.

    Retrieves most recent UA strings, up to a maximum of 20.

    :param amount: The amount of UA strings to retrieve
    :type amount: int
    :returns: List of UA strings
    :rtype: list

    :Example:

    >>> import browserinfo
    >>> browserinfo.recent(1)
    ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36']

    """

    return _getResults(amount, recentXpath)
