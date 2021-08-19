# решить задачу генерации нечетных чисел от 1 до n (включительно), не используя yield

n = int(input('Введите число: '))
odd_to_15 = (num for num in range (1, n  +1, 2))
print(next (odd_to_15)) #1
print(next (odd_to_15)) #3
print(next (odd_to_15)) #5
