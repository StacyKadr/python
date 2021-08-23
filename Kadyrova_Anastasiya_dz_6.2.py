#  Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    list_addr = [line[:line.find(' ')] for line in f]

print(max(set(list_addr), key=list_addr.count))