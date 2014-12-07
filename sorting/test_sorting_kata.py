from unittest import TestCase


def sort(list):
    return list


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assertEquals(None, sort(None))

    def test_given_empty_list__should_return_empty_list(self):
        self.assertEquals([], sort([]))