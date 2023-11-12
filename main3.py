import os
import datetime
from iterator import FlatIterator


def logger(old_function):

    def new_function(*args, **kwargs):
        main = "main.log"
        with open(main, 'a') as f:
            f.writelines(f"Вызываю функцию {old_function.__name__}. ")
            f.writelines(f"дата и время вызова функции {datetime.datetime.now()}. ")
            f.writelines(f"С аргументами {args} и {kwargs}. ")
            result = old_function(*args, **kwargs)
            f.writelines(f"Получил результат {result}.")
            f.writelines("\n------------------\n")
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def flat_list(list_of_lists):
        f = (list(FlatIterator(list_of_lists)))
        return f

    flat_list([[1, 2], [3], [4]])

if __name__ == '__main__':
    test_1()
