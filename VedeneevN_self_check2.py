"""
Веденеев Никита Александрович
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Веденеев Никита Александрович'
i = 5

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл while добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""
i = 0
ind = 0
fio.append([])
while i != len(s):
    if s[i] == ' ':
        fio.append([])
        ind += 1
        i +=1
    else:
        fio[ind].append(s[i])
        i += 1

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['В', 'е', 'д', 'е', 'н', 'е', 'е', 'в'], ['Н', 'и', 'к', 'и', 'т', 'а'], ['А', 'л', 'е', 'к', 'с', 'а', 'н', 'д', 'р', 'о', 'в', 'и', 'ч']]))

""" Задание №3
Используя цикл for переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

for i, letter in enumerate(fio):
    fio[i] = fio[i][::-1]
    

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['в', 'е', 'е', 'н', 'е', 'д', 'е', 'В'], ['а', 'т', 'и', 'к', 'и', 'Н'], ['ч', 'и', 'в', 'о', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А']]))

""" Задание №4
Получите из переменной fio 2-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][-2]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'и'))

""" Задание №5
Получите из переменной fio 2-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][-2]
"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'и'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len =[len(fio[0]), len(fio[1]), len(fio[2])]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [8, 6, 13]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(fio_len)

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 6))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""
i = 0
chars = str()
while i < min_len:
    for j in range(len(fio)):
        chars += fio[j][i]
    i += 1
"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'вачетиеивнкоеирдНд'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""

reversed_fio_dict = {'фамилия':fio[0],   'имя': fio[1],    'отчество': fio[2]}

"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['в', 'е', 'е', 'н', 'е', 'д', 'е', 'В'], 'имя': ['а', 'т', 'и', 'к', 'и', 'Н'], 'отчество': ['ч', 'и', 'в', 'о', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values())

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['в', 'е', 'е', 'н', 'е', 'д', 'е', 'В'], ['а', 'т', 'и', 'к', 'и', 'Н'], ['ч', 'и', 'в', 'о', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(reversed_fio_dict.items())

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['в', 'е', 'е', 'н', 'е', 'д', 'е', 'В']), ('имя', ['а', 'т', 'и', 'к', 'и', 'Н']), ('отчество', ['ч', 'и', 'в', 'о', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = reversed_fio_dict.get('фамилия')
"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['в', 'е', 'е', 'н', 'е', 'д', 'е', 'В']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = s.replace(' ','').lower()

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'веденеевникитаалександрович'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

res = {}

for i in s:
    res[i] = s.count(i)
res = list(res.items())

"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('в', 3), ('е', 5), ('д', 2), ('н', 3), ('и', 3), ('к', 2), ('т', 1), ('а', 3), ('л', 1), ('с', 1), ('р', 1), ('о', 1), ('ч', 1)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию nikitaCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов nikitaCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def nikitaCharToIndex(char: str) -> int:
    simbol = char.lower()
    return letters.find(simbol)+1 

"""------------ конец блока редактирования----------------"""

print('№17 ' + str(nikitaCharToIndex("Ъ") == 28))

""" Задание №18
При помощи функции nikitaCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""

for i in range(len(fio)):
    k = 0
    s = []
    while k < len(fio[i]):
        s.append(nikitaCharToIndex(fio[i][k]))
        k+=1
    fio[i] = s

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[3, 6, 6, 15, 6, 5, 6, 3], [1, 20, 10, 12, 10, 15], [25, 10, 3, 16, 18, 5, 15, 1, 19, 12, 6, 13, 1]]))


""" +++ КОНЕЦ =) +++ """
