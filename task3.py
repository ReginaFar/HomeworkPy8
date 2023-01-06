# Задание 3.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        num_1 = int(input("Введите делимое:"))
        num_2 = int(input("Введите делитель:"))
        if num_2 == 0:
            raise OwnError("Нельзя делить на 0!")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Вы ввели не число!"
    except OwnError as err:
        return err


print(division())
