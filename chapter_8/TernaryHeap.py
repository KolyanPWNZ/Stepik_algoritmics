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
        if node.left is None:
            node.left = TreeNode(value)
        elif node.middle is None:
            node.middle = TreeNode(value)
        elif node.right is None:
            node.right = TreeNode(value)
        else:
            # Если все потомки заполнены, рекурсивно вызываем _insert
            # на левом потомке для балансировки дерева
            self._insert(node.left, value)

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

    def display_nodes(self):
        if self.root is None:
            print("Куча пуста.")
            return

        self._display_nodes_recursive(self.root, level=0)

    def _display_nodes_recursive(self, node, level):
        if node:
            # Выводим информацию о текущем узле
            print(f"узел {node.value}:")
            print(f"  число узла: {node.value}")
            print(f"  его лепестки:", end=" ")

            # Выводим значения лепестков текущего узла
            if node.left:
                print(node.left.value, end=", ")
            if node.middle:
                print(node.middle.value, end=", ")
            if node.right:
                print(node.right.value, end=" ")

            print()  # Переход на новую строку

            # Рекурсивно обходим лепестки
            self._display_nodes_recursive(node.left, level + 1)
            self._display_nodes_recursive(node.middle, level + 1)
            self._display_nodes_recursive(node.right, level + 1)

    def find_node(self, value):
        if self.root is None:
            return None
        return self._find_node_recursive(self.root, value)

    def _find_node_recursive(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node

        # Рекурсивный поиск во всех поддеревьях
        left_result = self._find_node_recursive(node.left, value)
        if left_result:
            return left_result

        middle_result = self._find_node_recursive(node.middle, value)
        if middle_result:
            return middle_result

        right_result = self._find_node_recursive(node.right, value)
        if right_result:
            return right_result


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

    def insert(self, value):
        if not self.value:
            assert "empty node"
        if not self.left:
            self.left = value
        elif not self.middle:
            self.middle = value
        elif not self.right:
            self.right = value
