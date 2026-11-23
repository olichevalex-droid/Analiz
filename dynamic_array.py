class Array:
    """Динамический массив: сам увеличивается, когда место заканчивается."""

    def __init__(self):
        self._capacity = 4                    # сколько ячеек выделено
        self._data = [None] * self._capacity  # сами ячейки
        self._size = 0                        # сколько ячеек занято

    def _grow(self):
        """Увеличить массив в 2 раза и перенести в него элементы."""
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def _check_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("индекс вне границ массива")

    def add(self, value):
        """Добавить элемент в конец."""
        if self._size == self._capacity:
            self._grow()
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        self._check_index(index)
        return self._data[index]

    def set(self, index, value):
        self._check_index(index)
        self._data[index] = value

    def remove(self, index):
        """Удалить элемент по индексу и вернуть его.
        Все элементы справа сдвигаются влево."""
        self._check_index(index)
        removed = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return removed

    def size(self):
        return self._size
