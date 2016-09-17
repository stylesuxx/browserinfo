from nose.tools import assert_equal

from browserinfo import recent, popular


class testBrowserInfo():
    def test_most_recent(self):
        results = recent(1)

        print results
        assert_equal(len(results), 1)

    def test_10_most_recent(self):
        results = recent(10)

        print results
        assert_equal(len(results), 10)

    def test_20_most_recent(self):
        results = recent(20)

        print results
        assert_equal(len(results), 20)

    def test_most_popular(self):
        results = popular(1)

        print results
        assert_equal(len(results), 1)

    def test_10_most_popular(self):
        results = popular(10)

        print results
        assert_equal(len(results), 10)

    def test_20_most_popular(self):
        results = popular(20)

        print results
        assert_equal(len(results), 20)

    def test_negative_amount_sanitization(self):
        results = popular(-1)

        print results
        assert_equal(len(results), 0)

    def test_positive_amount_sanitization(self):
        results = popular(100)

        print results
        assert_equal(len(results), 20)
