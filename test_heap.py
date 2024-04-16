from min_heap import MinHeap
import unittest

class TestMinHeap(unittest.TestCase):
    def test_pop_list(self):
        heap = MinHeap()
        items = [
            ('d', 4),
            ('h', 8),
            ('e', 5),
            ('c', 3),
            ('a', 1),
            ('b', 2),
            ('f', 6),
            ('g', 7),
        ]

        for key, value in items:
            heap.add(key, value)

        expected = sorted(items)
        expected_iter = iter(expected)

        while len(heap):
            item = next(expected_iter)
            self.assertEqual(item, heap.peek())
            self.assertEqual(item, heap.pop())


if __name__ == '__main__':
    unittest.main()
