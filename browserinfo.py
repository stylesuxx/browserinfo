"""Lightweight API wrapper for
`browser-info.net <http://www.browser-info.net/useragents>`_.
"""

from lxml import html
import urllib


baseUrl = 'http://www.browser-info.net/useragents'
recentXpath = ('(//div[@class="datatable"])[1]//tr/td[2]/a/text()')
popularXpath = ('(//div[@class="datatable"])[2]//tr/td[2]/a/text()')


def recent(amount=20):
    """Fetches UA strings.

    Retrieves most recent UA strings, up to a maximum of 20.

    :param amount: The amount of UA strings to retrieve
    :type amount: int
    :returns: List of UA strings

    :Example:

    >>> import browserinfo
    >>> browserinfo.recent(1)
    ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36']

    """

    f = urllib.urlopen(baseUrl)
    tree = html.fromstring(f.read())
    items = tree.xpath(recentXpath)

    return items[:amount]


def popular(amount=20):
    """Docstring for most recent"""

    f = urllib.urlopen(baseUrl)
    tree = html.fromstring(f.read())
    items = tree.xpath(popularXpath)

    return items[:amount]
