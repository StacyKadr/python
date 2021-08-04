#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#* в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int (input ("Введите количество секунд: "))
if duration >= 1 and duration <= 59:
    print (duration, "sec")
elif duration >= 60 and duration <= 3600:
    print (duration // 60, "min", duration % 60, "sec")
elif duration >= 3600 and duration <= 86400:
    print (duration // 3600, "hour", duration % 3600 // 60, "min", duration % 60, "sec")
else:
    duration >= 86400
    print (duration //86400, "days", duration % 86400 // 3600, "hour", duration % 86400 % 3600 // 60, "min", duration % 86400 % 3600 % 60 % 60, "sec")



