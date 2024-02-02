#("Ввведите первое число: ", int(input() )
import math
first = str(input("Что вы хотите сделать?: "))
#first_one = int(input("Введите число: "))
first_two = "найти корень"
second = "сложить числа"
third = "вычесть числа"
fourth = "перемножить числа"
fifth = "разделить числа"
#a = int(input("Ввведите первое число: "))
#b = int(input("Ввведите второе число: "))
if first == (first_two):
    first_one = (int(input("Введите число: ")))
    print("Корень равен: ", math.sqrt(first_one))
    print("Спасибо за использование!")
elif(first == (second)):
    a = int(input("Ввведите первое число: "))
    b = int(input("Ввведите второе число: "))
    print("Сумма равна:", a+b)
    print("Спасибо за использование!")
elif(first == (third)):
    a = int(input("Ввведите первое число: "))
    b = int(input("Ввведите второе число: "))
    print("Разность равна:", a-b)
    print("Спасибо за использование!")
elif(first == (fourth)):
    a = int(input("Ввведите первое число: "))
    b = int(input("Ввведите второе число: "))
    print("Произведение равно:", a*b)
    print("Спасибо за использование!")
elif(first == (fourth)):
    a = int(input("Ввведите первое число: "))
    b = int(input("Ввведите второе число: "))
    print("Частное равно:", a/b)
    print("Спасибо за использование!")
#else:
    #print("Спасибо за использование!")



#a = int(input("Ввведите первое число: "))
#b = int(input("Ввведите второе число: "))