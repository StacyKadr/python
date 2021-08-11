#*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}
def num_translate_adv ():
    number = input ('Введите число на английском: ')
    if number.istitle():
        print(numbers.get(number.lower()).title())
    else:
        print(numbers.get(number))

num_translate_adv ()
