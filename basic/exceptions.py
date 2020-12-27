
class DictEmptyException(Exception):

    def __init__(self, value, *args):
        super().__init__(*args)
        self.value = value


def my_super_sum(a, b):
    return a + b


def sum_my_dict(my_dict):
    if not my_dict:
        raise DictEmptyException(100, "You should pass non empty dict to call this function")
    the_sum = sum(my_dict.values())
    return the_sum, the_sum / len(my_dict)


def main(my_dict):
    try:
        print(sum_my_dict(my_dict))
    except DictEmptyException as e:
        print(f"Dict was empty {e}")
        return 0
    except (TypeError, ZeroDivisionError) as e:
        print(f"Some exception {e}")
    except Exception as e:
        print("Something goes wrong")
    finally:
        print("Finally")

print("===================\n"
      "Call with empty dict\n")
main({})
print("===================\n"
      "Call with strings as values\n")
main({'a': 10, 'b': 'str'})
