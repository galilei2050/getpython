import random
from .human import Human


class Child(Human):

    def __init__(self, *args, parents, **kwargs):
        super().__init__(*args, **kwargs)
        self._parents = parents

    def is_parent(self, human):
        return human in self._parents
