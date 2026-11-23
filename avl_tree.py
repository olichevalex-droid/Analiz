class AVLNode:
    """Узел дерева: значение, левый и правый потомок, высота."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    """Высота узла (у пустого места высота 0)."""
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    """Разница высот левой и правой частей.
    В АВЛ-дереве она всегда должна быть -1, 0 или 1."""
    return height(node.left) - height(node.right) if node else 0


def rotate_right(y):
    """Правый поворот: поднимаем левого потомка наверх."""
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y)
    update_height(x)
    return x


def rotate_left(x):
    """Левый поворот: поднимаем правого потомка наверх."""
    y = x.right
    x.right = y.left
    y.left = x
    update_height(x)
    update_height(y)
    return y


def insert(node, value):
    """Вставить значение и вернуть новый корень поддерева."""
    # 1. Обычная вставка, как в бинарном дереве поиска
    if node is None:
        return AVLNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    else:
        return node  # одинаковые значения не храним

    # 2. Обновляем высоту
    update_height(node)

    # 3. Проверяем баланс и при необходимости поворачиваем
    balance = balance_factor(node)

    if balance > 1 and value < node.left.value:    # левый-левый случай
        return rotate_right(node)
    if balance < -1 and value > node.right.value:  # правый-правый случай
        return rotate_left(node)
    if balance > 1 and value > node.left.value:    # левый-правый случай
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and value < node.right.value:  # правый-левый случай
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


def contains(node, value):
    """Есть ли значение в дереве."""
    while node is not None:
        if value == node.value:
            return True
        node = node.left if value < node.value else node.right
    return False


def to_list(node):
    """Все значения по возрастанию (обход слева направо)."""
    if node is None:
        return []
    return to_list(node.left) + [node.value] + to_list(node.right)
