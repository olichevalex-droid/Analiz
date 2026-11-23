def quick_sort(items):
    """Быстрая сортировка.

    1. Берём "опорный" элемент (середину списка).
    2. Делим остальные на три группы: меньше, равные и больше опорного.
    3. Так же сортируем "меньшие" и "большие" и склеиваем всё вместе.
    Возвращает новый отсортированный список.
    """
    if len(items) <= 1:  # пустой список или один элемент уже отсортирован
        return list(items)

    pivot = items[len(items) // 2]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
