from nose.tools import assert_equal

import browserinfo


class testBrowserInfo():
    def test_most_recent(self):
        results = browserinfo.recent(1)

        print results
        assert_equal(len(results), 1)

    def test_10_most_recent(self):
        results = browserinfo.recent(10)

        print results
        assert_equal(len(results), 10)

    def test_20_most_recent(self):
        results = browserinfo.recent(20)

        print results
        assert_equal(len(results), 20)

    def test_most_popular(self):
        results = browserinfo.popular(1)

        print results
        assert_equal(len(results), 1)

    def test_10_most_popular(self):
        results = browserinfo.popular(10)

        print results
        assert_equal(len(results), 10)

    def test_20_most_popular(self):
        results = browserinfo.popular(20)

        print results
        assert_equal(len(results), 20)

    def test_negative_amount_sanitization(self):
        results = browserinfo.popular(-1)

        print results
        assert_equal(len(results), 0)

    def test_positive_amount_sanitization(self):
        results = browserinfo.popular(100)

        print results
        assert_equal(len(results), 20)

    def test_dom_exception_repo_link(self):
        err = browserinfo.DOMChanged()

        print err
        assert browserinfo.__repository__ in err.message
