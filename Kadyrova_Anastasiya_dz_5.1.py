# написать генератор нечетных чисел от 1 до n (включительно), используя ключевое слово yield

def odd_number(n):
    for num in range (1, n + 1, 2):
        yield num

odd_to_15 = odd_number(15)
print(next (odd_to_15)) #1
print(next (odd_to_15)) #3
print(next (odd_to_15)) #5
