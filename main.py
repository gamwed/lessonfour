# text = input('numbers=')
# x = text.split()
# x = list(map(int, x))
#
# print(x)
# mid = len(x)//2
# y = x[:mid]
# z = x[mid:]
# print(y, z)

# Task 1
# num = input("4значне число ")
# if len(num) !=4:
#     print("Я сказав 4значне!")
# else:
#     num = list(map(int, num))
#     left_site = num[0] + num[1]
#     right_site = num[2] + num[3]
#     if left_site == right_site:
#         print("Счастя у квитку!!")
#     else:
#         print("невдача ((")

# task 2
# num = input("Введіть шестизначне число: ")
#
# if len(num) != 6:
#     print("Неправильна кількість цифр. Будь ласка, введіть шестизначне число.")
# else:
#     reversed_num = num[::-1]  # Реверсуємо число
#
#     if num == reversed_num:
#         print("Це паліндром!")
#     else:
#         print("Це не паліндром.")

# task 3
x = float(input("Введіть координату x точки: "))
y = float(input("Введіть координату y точки: "))

distance_squared = x ** 2 + y ** 2  # Квадрат відстані від початку координат до точки
radius_squared = 4 ** 2  # Квадрат радіусу кола

if distance_squared <= radius_squared:
    print("Точка лежить всередині кола.")
else:
    print("Точка не лежить всередині кола.")