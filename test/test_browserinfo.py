from nose.tools import assert_equal

from browserinfo.Browserinfo import mostRecent


class testBrowserInfo():
    def test_most_recent(self):
        results = mostRecent()

        print results
        assert_equal(len(results), 20)

    def test_10_most_recent(self):
        results = mostRecent(10)

        print results
        assert_equal(len(results), 10)

    def test_100_most_recent(self):
        results = mostRecent(100)

        print results
        assert_equal(len(results), 20)
