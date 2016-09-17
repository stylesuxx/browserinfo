from lxml import html
import urllib

baseUrl = 'http://www.browser-info.net/useragents'
recentXpath = ('(//div[@class="datatable"])[1]//tr/td[2]/a/text()')
popularXpath = ('(//div[@class="datatable"])[1]//tr/td[2]/a/text()')


def mostRecent(amount=20):
    f = urllib.urlopen(baseUrl)
    tree = html.fromstring(f.read())
    items = tree.xpath(recentXpath)

    return items[:amount]


def mostPopular(amount):
    f = urllib.urlopen(baseUrl)
    tree = html.fromstring(f.read())
    item = tree.xpath(popularXpath)

    return items[:amount]
