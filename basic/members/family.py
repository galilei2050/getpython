import random
from datetime import datetime
from .human import Human
from .child import Child


class Family(object):
    def __init__(self, *members):
        self._members = list(members)

    def __len__(self):
        return len(self._members)

    def __contains__(self, item):
        return item in self._members

    def born(self, name):
        if len(self._members) < 2:
            return None
        child = Child(parents=self._members[:2], name=name, sex=random.choice(Human.SEX), birthday=datetime.now())
        self._members.append(child)
        return child

    def age(self):
        return sum([m.age() for m in self._members])/len(self._members)