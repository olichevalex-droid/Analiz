class Node:
    """Один "вагончик" списка: хранит значение и ссылку на следующий."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Односвязный список."""

    def __init__(self):
        self.head = None  # первый элемент (None, если список пуст)
        self._size = 0

    def add(self, value):
        """Добавить элемент в конец списка."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:  # идём до последнего элемента
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, value):
        """Удалить первый элемент с таким значением.
        Возвращает True, если удалили, и False, если такого нет."""
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:  # удаляем первый элемент
                    self.head = current.next
                else:  # "перепрыгиваем" через удаляемый
                    previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
        return False

    def contains(self, value):
        """Есть ли значение в списке."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def size(self):
        return self._size

    def to_list(self):
        """Превратить в обычный список Python (удобно для тестов)."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
