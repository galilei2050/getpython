from datetime import datetime
from members import Human, Family


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