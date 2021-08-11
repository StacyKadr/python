#Реализовать функцию get_jokes(), возвращающую n шуток,
#сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
from random import choice

def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    for i in range(n):
        jokes_list.append(f' {choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    print (jokes_list)

get_jokes(5)
