from nose.tools import assert_equal

from browserinfo import recent, popular


class testBrowserInfo():
    def test_most_recent(self):
        results = recent()

        print results
        assert_equal(len(results), 20)

    def test_10_most_recent(self):
        results = recent(10)

        print results
        assert_equal(len(results), 10)

    def test_100_most_recent(self):
        results = recent(100)

        print results
        assert_equal(len(results), 20)

    def test_most_popular(self):
        results = popular()

        print results
        assert_equal(len(results), 20)

    def test_10_most_popular(self):
        results = popular(10)

        print results
        assert_equal(len(results), 10)

    def test_100_most_popular(self):
        results = popular(100)

        print results
        assert_equal(len(results), 20)
