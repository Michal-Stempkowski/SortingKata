from copy import copy
from itertools import chain
from random import randrange
from unittest import TestCase


def select_random_pivot(unsorted):
    return unsorted[randrange(0, len(unsorted))]


def sort(unsorted):
    if unsorted and len(unsorted) > 1:
        pivot = select_random_pivot(unsorted)

        lesser = sort(list(filter(lambda x: x < pivot, unsorted)))
        equal = filter(lambda x: x == pivot, unsorted)
        greater = sort(list(filter(lambda x: x > pivot, unsorted)))

        return list(chain(lesser, equal, greater))

    return unsorted


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assert_sorted(None, None)

    def assert_sorted(self, sorted, unsorted):
        self.assertEquals(sorted, sort(unsorted))

    def test_given_empty_list__should_return_empty_list(self):
        self.assert_sorted([], [])
        self.assert_sorted([1, 2], [2, 1])
        self.assert_sorted([1, 2, 3, 4], [4, 3, 2, 1])