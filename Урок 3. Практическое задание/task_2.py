"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib
from uuid import uuid4

passwd_1 = input('Введите пароль: ')
salt = uuid4().hex
hash_passwd_1 = hashlib.sha256(passwd_1.encode()+salt.encode()).hexdigest()
print(hash_passwd_1)

with open("hash.txt", 'w') as file:
    file.write(hash_passwd_1)

passwd_2 = input('Введите пароль еще раз для проверки: ')
hash_passwd_2 = hashlib.sha256(passwd_2.encode()+salt.encode()).hexdigest()
print(hash_passwd_2)

with open("hash.txt") as file:
    if hash_passwd_2 == file.read():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')

