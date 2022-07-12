from django.http import Http404
from random import randint, choice


def url_generator(url=r'https://planx.one/verylongurl...', n=6):
    '''
    Преобразователь URL-адресов в короткие и уникальные
    :param url: оригинальный URL-адрес, который вводит пользователь
    :param n: количество символов, которое сгенерирует программа после домена. По умолчанию - 6 символов
    :return: уникальный короткий URL-адрес
    '''
    lst_numbers = list(range(10))
    lst_symbols = [chr(x) for x in range(65, 123) if x not in [91, 92, 93, 94, 95, 96]]
    dct = {0: lst_numbers, 1: lst_symbols}
    lst_url = url.split('/')
    address = lst_url[0] + '//' + lst_url[2] + '/'  # создаем первую часть url из протокола и домена
    for x in range(n):  # добавляем вторую часть к url-адресу путем генерации строки, которая имеет длину n
        address += str(choice(dct[randint(0, 1)]))
    return address


def test_url_generator(f, n=100_000):
    '''
    Тестируем вероятность совпадения URL-ов при введении разными пользователями одно и того же адреса.
    И видим, что адреса не уникальны: Длинна_1: 100000; Длинна_2: 99994
    Способ решения: увеличить параметр n(количество генерируемых символов) в url_generator, например на единицу
    '''
    lst = []
    for i in range(n):
        lst.append(f())
    print(f'Длинна_1: {len(lst)}\n'
          f'Длинна_2: {len(set(lst))}')


# test_url_generator(url_generator)
