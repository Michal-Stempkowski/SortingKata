from itertools import chain
from random import randrange
from unittest import TestCase


def select_random_pivot(unsorted):
    return unsorted[randrange(0, len(unsorted))]


def sort(unsorted):
    if unsorted and len(unsorted) > 1:
        pivot = select_random_pivot(unsorted)

        lesser = filter(lambda x: x < pivot, unsorted)
        equal = filter(lambda x: x == pivot, unsorted)
        greater = filter(lambda x: x > pivot, unsorted)

        return list(chain(lesser, equal, greater))

    return unsorted


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assertEquals(None, sort(None))

    def test_given_empty_list__should_return_empty_list(self):
        self.assertEquals([], sort([]))
        self.assertEquals([1, 2], sort([2, 1]))