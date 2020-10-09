

# 2*({3+4}*10 -1)

brackets = {
    '(': ')',
    '{': '}'
}


def is_right_math(equation):
    stack = list()
    for c in equation:
        if c in brackets:
            stack.append(c)
        if c in brackets.values():
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if brackets[last_open] != c:
                return False

    return len(stack) == 0   # (2+30


class Stack():
    def __init__(self):
        self._data = []

    def put(self, value):
        # average O(1)
        # O(n) - worst case
        self._data.append(value)

    def get(self):
        # O(1) - average
        # O(n) - worst case
        return self._data.pop()


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next:
            return f'{self.value} -> {self.next.value}'

        return f'{self.value} -> None'


class Stack():

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def put(self, value):
        self._root = Node(value, self._root)
        self._size += 1

    def get(self):
        if self._root is None:
            return None
        value = self._root.value
        self._root = self._root.next
        self._size -= 1
        return value


def Node():
    def __init__(self, value, next, prev):
        self.next = next
        self.prev = prev
        self.value = value
