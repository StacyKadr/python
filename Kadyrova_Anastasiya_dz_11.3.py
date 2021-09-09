class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number = input('Введите число: ')
while type(number) != int and number != 'stop':
    try:
        number = int(number)
    except ValueError:
        print('Введено не число')
        number = input('Введите число: ')
        while number == 'stop':
            break
    else:
        print(f'Результат: {number}')
        number = input('Введите число: ')
