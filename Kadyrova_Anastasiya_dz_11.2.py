class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data_one = input('Введите делимое: ')
inp_data_two = input('Введите делитель: ')

try:
    inp_data_two = int(inp_data_two)
    inp_data_one = int(inp_data_one)
    if inp_data_two == 0:
        raise OwnError('Деление на ноль недопустимо!')
except ValueError:
    print('Введено не число')
except OwnError as err:
    print(err)
else:
    print(f'Результат деления: {inp_data_one / inp_data_two}')
