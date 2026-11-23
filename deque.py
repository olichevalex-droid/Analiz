class DNode:
    """Элемент дека: знает и предыдущего, и следующего соседа."""

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    """Дек: добавлять и забирать элементы можно с обоих концов."""

    def __init__(self):
        self.front = None  # левый край
        self.back = None   # правый край
        self._size = 0

    def add_front(self, value):
        """Добавить в начало."""
        node = DNode(value)
        if self.front is None:  # дек пуст
            self.front = self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self._size += 1

    def add_back(self, value):
        """Добавить в конец."""
        node = DNode(value)
        if self.back is None:  # дек пуст
            self.front = self.back = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node
        self._size += 1

    def remove_front(self):
        """Забрать элемент из начала."""
        if self.front is None:
            raise IndexError("дек пуст")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # элементов не осталось
            self.back = None
        else:
            self.front.prev = None
        self._size -= 1
        return value

    def remove_back(self):
        """Забрать элемент из конца."""
        if self.back is None:
            raise IndexError("дек пуст")
        value = self.back.value
        self.back = self.back.prev
        if self.back is None:  # элементов не осталось
            self.front = None
        else:
            self.back.next = None
        self._size -= 1
        return value

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0
