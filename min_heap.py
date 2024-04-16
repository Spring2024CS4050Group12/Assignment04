from collections import namedtuple


class MinHeap:
    """
    A min-heap of (`key`, `value`) pairs.

    A `key` is just some arbitrary value the user can associate with the `value`.
    A `value` is the value that determines the order of elements in the heap.

    The value of a parent is always less than or equal to the value of its child.

    Basically, think of this as a dictionary supports the following:
    - Add a key value pair
    - Get and/or remove the key associated with the smallest value in
      logarithmic time
    - Decrease the value associated with a key

    Implementation details:
        - `_mapping` is a map from the `key` in each pair to the index in the `_lyst`
        - `_lyst` is 1-indexed (index 0 is filled with a placeholder)
    """

    Entry = namedtuple('Entry', ('key', 'value'))

    # TODO: support heapify() in constructor
    def __init__(self):
        # 1-indexing is easier and since we have to put something here anyway,
        # might as well use something that makes the bubble-up procedure
        # simpler :)
        self._lyst = [self.Entry(object(), float('-inf'))]
        self._mapping = {}
    
    def __len__(self):
        return len(self._lyst) - 1
    
    def __getitem__(self, key):
        if key not in self:
            raise KeyError(f"The key '{key}' is not in heap!")

        return self._lyst[self._mapping[key]].value
    
    def __contains__(self, key):
        return key in self._mapping
    
    def _swap(self, i, j):
        self._lyst[i], self._lyst[j] = self._lyst[j], self._lyst[i]

        self._mapping[self._lyst[i].key] = i
        self._mapping[self._lyst[j].key] = j

    def _bubble_up(self, i):
        parent = i // 2
        if self._lyst[parent].value <= self._lyst[i].value:
            return i

        self._swap(i, parent)
        self._bubble_up(parent)
    
    def _percolate(self, i):
        left_child = 2 * i
        right_child = left_child + 1

        value = self._lyst[i].value
        left_value = self._lyst[left_child].value if left_child < len(self._lyst) else float('inf')
        right_value = self._lyst[right_child].value if right_child < len(self._lyst) else float('inf')

        if left_value < min(value, right_value):
            self._swap(i, left_child)
            return self._percolate(left_child)

        if right_value < min(value, left_value):
            self._swap(i, right_child)
            return self._percolate(right_child)

        return i
    
    def add(self, key, value):
        i = len(self._lyst)

        self._lyst.append(self.Entry(key, value))

        self._bubble_up(i)

    def peek(self):
        return self._lyst[1]

    def pop(self):
        if len(self) == 0:
            raise ValueError("Heap is empty!")
        
        if len(self) == 1:
            return self._lyst.pop()
        
        min_entry = self._lyst[1]
        self._lyst[1] = self._lyst.pop()

        self._percolate(1)

        return min_entry

    def decrease_value(self, key, new_value):
        if key not in self:
            raise KeyError(f"The key '{key}' is not in heap!")
        
        i = self._mapping[key]

        old_value = self._lyst[i].value
        if old_value <= new_value:
            return old_value
        
        self._lyst[i] = self.Entry(key, new_value)
        self._bubble_up(i)

        return new_value