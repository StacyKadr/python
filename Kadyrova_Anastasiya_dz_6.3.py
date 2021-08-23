#  Написать код, загружающий данные из 2 файлов и формирующий из них словарь: ключи — ФИО,
#  значения — данные о хобби.

from json import dump
from itertools import zip_longest

with open('users.csv', 'r') as users:
    with open('hobby.csv', 'r') as hobby:
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open ("dict.json", "w", encoding="utf-8") as f:
                main_list=zip_longest((" ".join(us.split(",")) for us in users),hobby,fillvalue=None)
                my_dict={str(el[0]).strip(): str(el[1]).strip() for el in main_list}
                dump(my_dict, f, ensure_ascii=False, indent=4)
                print(my_dict)
        else:
            exit(1)
