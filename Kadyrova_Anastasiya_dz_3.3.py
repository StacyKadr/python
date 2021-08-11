#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
def thesaurus (*args):
    new_dict = {}
    for n in args:
        key = n [0].capitalize()
        if key not in new_dict:
            new_dict[key] =[]
        new_dict[key].append(n)
    return new_dict
print(thesaurus("Иван", "Мария", "Петр", "Илья"))