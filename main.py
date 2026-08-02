# Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.
import pyfiglet
from colorama import Fore, Style, init
from datetime import datetime

from db.people import get_people
from application.salary import calculate_salary


if __name__ == "__main__":

    # получаем данные о человеке если таковой имеется в списке
    print(get_people('Alice'))

    # Высчтываем зарплату из оклада и бонуса в процентах
    print(calculate_salary(5000, 10))

    # Получаем текущую дату и вермя и выводим их в формате "день.месяц.год часы:минуты:секунды"
    print(f"Current date and time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

    # Инициализируем colorama (обязательно для Windows)
    init(autoreset=True)

    # Создаем большой текст с помощью pyfiglet
    ascii_art = pyfiglet.figlet_format(input("Введите текст: "))

    # Выводим его разными цветами
    print(Fore.MAGENTA + ascii_art)
    print(Fore.CYAN + ascii_art)

