from collections import deque

class TernaryHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)  # Создаем новый узел, если текущий узел None

        # Выбираем поддерево для вставки
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.middle = self._insert(node.middle, value)
        # Не вставляем дубликаты

        return node

    def extract_max(self):
        if self.root is None:
            return None

        max_value = self._find_max(self.root)
        self._remove_max(self.root, max_value)
        return max_value

    def _find_max(self, node):
        max_value = node.value
        if node.left:
            max_value = max(max_value, self._find_max(node.left))
        if node.middle:
            max_value = max(max_value, self._find_max(node.middle))
        if node.right:
            max_value = max(max_value, self._find_max(node.right))
        return max_value

    def _remove_max(self, node, value):
        if node.value == value:
            node.value = float("-inf")
        if node.left:
            self._remove_max(node.left, value)
        if node.middle:
            self._remove_max(node.middle, value)
        if node.right:
            self._remove_max(node.right, value)

    def find_parent(self, value):
        if self.root:
            return self._find_parent(self.root, value, None)

    def _find_parent(self, node, value, parent):
        if node is None:
            return None

        if node.value == value:
            return parent

        parent = node  # Обновляем родителя

        left_result = self._find_parent(node.left, value, parent)
        if left_result:
            return left_result

        middle_result = self._find_parent(node.middle, value, parent)
        if middle_result:
            return middle_result

        right_result = self._find_parent(node.right, value, parent)
        if right_result:
            return right_result

    def display(self):
        if self.root is None:
            print("Куча пуста.")
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.middle:
                queue.append(node.middle)
            if node.right:
                queue.append(node.right)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None