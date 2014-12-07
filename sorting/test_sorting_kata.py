from copy import copy
from unittest import TestCase


def swap(some_list, left, right):
    tmp = some_list[left]
    some_list[left] = some_list[right]
    some_list[right] = tmp


def sort(unsorted):
    is_sort_required = unsorted and len(unsorted) > 1

    while is_sort_required:
        last_element_index = len(unsorted) - 1
        is_sort_required = False

        for current in range(0, last_element_index):
            next = current + 1

            if unsorted[current] > unsorted[next]:
                swap(unsorted, current, next)
                is_sort_required = True

    return unsorted


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assert_sorted(None, None)

    def test_given_empty_list__should_return_empty_list(self):
        self.assert_sorted([], [])

    def assert_sorted(self, sorted, unsorted):
        self.assertEquals(sorted, sort(unsorted))

    def test_given_unsorted_list__should_sort_it(self):
        self.assert_sorted([1, 2], [2, 1])
        self.assert_sorted([0, 1, 2], [0, 2, 1])
        self.assert_sorted([0, 1, 2], [2, 1, 0])

        big_list = list(range(1000, 0, -1))
        big_list_sorted = copy(big_list)
        big_list_sorted.reverse()

        self.assert_sorted(big_list_sorted, big_list)