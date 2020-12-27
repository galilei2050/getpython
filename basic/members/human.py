from datetime import datetime

MATURE_AGE = 18


class Human(object):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    SEX = [MALE, FEMALE, OTHER]

    def __init__(self, birthday, sex, name):
        '''
        Human()
        :param birthday:
        :param sex:
        :param name:
        '''
        self.name = name
        self.birthday = birthday
        self.sex = sex

    def age(self):
        n = datetime.now()
        return int((n - self.birthday).days/365)

    def is_mature(self):
        return self.age() > MATURE_AGE

    def __repr__(self):
        return f'{self.name} was born {self.birthday}'

    def __hash__(self):
        return self.name + str(self.birthday)

    def __eq__(self, other):
        return self.name == other.name