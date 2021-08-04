#Склонение слова
#Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

number = int (input ("Введите число от 1 до 100: "))
if number > 10 and number < 20:
    print (number, "процентов")
elif number % 10 == 1:
    print (number, "процент")
elif number % 10 == 0 or (number % 10 > 5 and number % 10 <= 9):
    print(number, "процентов")
else:
    print(number, "процента")