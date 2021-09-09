class Data:
    def __init__(self, data_one):
        self.data_one = str(data_one)

    @classmethod
    def extract(cls, data_one):
        my_date = []
        for i in data_one.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return f'True'
        else:
            return f'False'

    def __str__(self):
        return f'Дата {Data.extract(self.data_one)}'

today = Data('09 - 09 - 2021')
print(today)