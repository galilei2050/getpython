import random
from datetime import datetime

MATURE_AGE = 18


class Human(object):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    SEX = [MALE, FEMALE, OTHER]

    def __init__(self, birthday, sex, name):
        self.name = name
        self.birthday = birthday

    def age(self):
        n = datetime.now()
        return int((n - self.birthday).days/365)

    def can_drink_alcohol(self):
        return self.age() > MATURE_AGE

    def __repr__(self):
        return f'{self.name} was born {self.birthday}'

    def __hash__(self):
        return self.name + str(self.birthday)

    def __eq__(self, other):
        return self.name == other.name


class Child(Human):

    def __init__(self, *args, parents, **kwargs):
        super().__init__(*args, **kwargs)
        self._parents = parents

    def is_parent(self, human):
        return human in self._parents


class Family(object):
    def __init__(self, *members):
        self._members = list(members)

    def __len__(self):
        return len(self._members)

    def __contains__(self, item):
        return

    def born(self, name):
        if len(self._members) < 2:
            return None
        child = Child(parents=self._members[:2], name=name, sex=random.choice(Human.SEX), birthday=datetime.now())
        self._members.append(child)
        return child

    def age(self):
        return sum([m.age() for m in self._members])/len(self._members)


def print_family_info(family):
    '''
    Функция печатает на экран информацию о семье
    :param family: семья
    :return:
    '''
    family_members = len(family)
    average_age = family.age()
    print(f'Family of {family_members} members. Average age is {average_age}')


def main():
    alex = Human(name='Alex', birthday=datetime(1987, 12, 12), sex=Human.MALE)
    print(alex)
    margo = Human(name='Margo', birthday=datetime(1991, 10, 12), sex=Human.FEMALE)
    print(margo)

    family = Family(alex, margo)
    print_family_info(family)

    child = family.born('Nick')
    print_family_info(family)

    if child.is_parent(alex):
        print(f'{alex.name} is parent of {child.name}')


if __name__ == '__main__':
    main()