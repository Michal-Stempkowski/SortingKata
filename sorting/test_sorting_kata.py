from unittest import TestCase


def sort(list):
    return None


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assertEquals(None, sort(None))