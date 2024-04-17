from min_heap import MinHeap
import unittest

class TestMinHeap(unittest.TestCase):
    def test_contains(self):
        heap = MinHeap()
        self.assertFalse('x' in heap)

        heap.add('x', 42)
        self.assertTrue('x' in heap)

        heap.pop()
        self.assertFalse('x' in heap)

    def test_peek_pop_len(self):
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

        expected = [
            ('a', 1),
            ('b', 2),
            ('c', 3),
            ('d', 4),
            ('e', 5),
            ('f', 6),
            ('g', 7),
            ('h', 8),
        ]

        for key, value in items:
            heap.add(key, value)

        for i, item in enumerate(expected):
            self.assertEqual(len(heap), len(expected) - i)
            self.assertEqual(item, heap.peek())
            self.assertEqual(item, heap.pop())
        
        self.assertEqual(len(heap), 0)
    
    def test_decrease_value(self):
        heap = MinHeap()
        heap.add('a', 1)
        heap.add('b', 2)
        heap.add('c', 3)

        self.assertEqual(heap.peek(), ('a', 1))
        self.assertEqual(heap['c'], 3)

        heap.decrease_value('c', 0)
        self.assertEqual(heap.peek(), ('c', 0))
        self.assertEqual(heap['c'], 0)

if __name__ == '__main__':
    unittest.main()
