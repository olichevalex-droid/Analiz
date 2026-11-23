import unittest

from bubble_sort import bubble_sort
from quick_sort import quick_sort
from dynamic_array import Array
from deque import Deque
from linked_list import LinkedList
from avl_tree import insert, to_list, height, contains


class TestSorts(unittest.TestCase):
    def check(self, sort_func):
        self.assertEqual(sort_func([]), [])
        self.assertEqual(sort_func([1]), [1])
        self.assertEqual(sort_func([3, 2, 1]), [1, 2, 3])
        self.assertEqual(sort_func([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        self.assertEqual(sort_func([2, 2, 1, 1]), [1, 1, 2, 2])
        self.assertEqual(sort_func([1, 2, 3]), [1, 2, 3])

    def test_bubble_sort(self):
        self.check(bubble_sort)

    def test_quick_sort(self):
        self.check(quick_sort)

    def test_original_not_changed(self):
        data = [3, 1, 2]
        bubble_sort(data)
        quick_sort(data)
        self.assertEqual(data, [3, 1, 2])


class TestLinkedList(unittest.TestCase):
    def test_add_and_remove(self):
        lst = LinkedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertTrue(lst.remove(2))
        self.assertEqual(lst.to_list(), [1, 3])
        self.assertTrue(lst.remove(1))
        self.assertEqual(lst.to_list(), [3])
        self.assertEqual(lst.size(), 1)

    def test_remove_missing(self):
        lst = LinkedList()
        lst.add(1)
        self.assertFalse(lst.remove(99))

    def test_contains(self):
        lst = LinkedList()
        lst.add(5)
        self.assertTrue(lst.contains(5))
        self.assertFalse(lst.contains(6))


class TestArray(unittest.TestCase):
    def test_add_get_set_remove(self):
        a = Array()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.get(0), 1)
        a.set(0, 10)
        self.assertEqual(a.get(0), 10)
        self.assertEqual(a.remove(1), 2)
        self.assertEqual(a.size(), 2)
        self.assertEqual(a.get(1), 3)

    def test_grow(self):
        a = Array()
        for i in range(100):  # больше начальной вместимости
            a.add(i)
        self.assertEqual(a.size(), 100)
        self.assertEqual(a.get(99), 99)

    def test_bad_index(self):
        a = Array()
        with self.assertRaises(IndexError):
            a.get(0)


class TestDeque(unittest.TestCase):
    def test_both_ends(self):
        d = Deque()
        d.add_back(2)
        d.add_front(1)
        d.add_back(3)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.remove_front(), 1)
        self.assertEqual(d.remove_back(), 3)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.remove_back(), 2)
        self.assertTrue(d.is_empty())

    def test_empty(self):
        d = Deque()
        with self.assertRaises(IndexError):
            d.remove_front()
        with self.assertRaises(IndexError):
            d.remove_back()


class TestAVLTree(unittest.TestCase):
    def test_sorted_output(self):
        root = None
        for x in [5, 3, 8, 1, 4]:
            root = insert(root, x)
        self.assertEqual(to_list(root), [1, 3, 4, 5, 8])

    def test_balance(self):
        # без балансировки 1..7 вытянулись бы в цепочку высотой 7
        root = None
        for x in range(1, 8):
            root = insert(root, x)
        self.assertEqual(height(root), 3)
        self.assertEqual(root.value, 4)

    def test_contains_and_duplicates(self):
        root = None
        for x in [2, 1, 3, 2]:
            root = insert(root, x)
        self.assertEqual(to_list(root), [1, 2, 3])
        self.assertTrue(contains(root, 3))
        self.assertFalse(contains(root, 10))


if __name__ == "__main__":
    unittest.main()
