from unittest import TestCase


def swap(some_list, left, right):
    tmp = some_list[left]
    some_list[left] = some_list[right]
    some_list[right] = tmp


def sort(unsorted):
    if not unsorted or len(unsorted) < 2:
        return unsorted

    if unsorted[0] > unsorted[1]:
        swap(unsorted, 0, 1)
    return unsorted


class TestSortingKata(TestCase):
    def setUp(self):
        pass

    def test_given_none__should_return_none(self):
        self.assertEquals(None, sort(None))

    def test_given_empty_list__should_return_empty_list(self):
        self.assertEquals([], sort([]))

    def test_given_unsorted_list__should_sort_it(self):
        self.assertEquals([1, 2], sort([2, 1]))