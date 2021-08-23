#  Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
#  логов web-сервера nginx_logs.txt

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    content = ((line.split()[0], line.split()[5], line.split()[6]) for line in f)
    for i in content:
        print (i)
