print("Выберите действие")
print("1 - Сложение")
print("2 - Вычитание")
print("3 - Умонжение")
print("4 - Деление")
print("5 - Квадратное уравнение")
add = 1
Sub = 2
Mult = 3
div = 4
equ = 5
n = int(input())
action = n
if n == 1:
    print("Введите первое слагаемое")
    number1 = float(input())
    print("Введите второе слагаемое")
    number2 = float(input())
    answer = number1 + number2
    print("Ответ", answer)
if n == 2:
    print("Введите уменьшаемое")
    number1 = float(input())
    print("Введите вычитаемое")
    number2 = float(input())
    answer = number1 - number2
    print("Ответ", answer)
if n == 3:
    print("Введите первый множитель")
    number1 = float(input())
    print("Введите второй множитель")
    number2 = float(input())
    answer = number1 * number2
    print("Ответ", answer)
if n == 4:
    print("Введите делимое")
    number1 = float(input())
    print("Введите делитель")
    number2 = float(input())
    answer = number1 / number2
    print("Ответ", answer)
if n == 5:
    print("Введите параметры кв. уравнения")
    print("a =")
    a = float(input())
    print("b =")
    b = float(input())
    print("c =")
    c = float(input())
    D = b**2 - 4 * a * c
    if D > 0:
       x1 = (-b + D**0.5) / 2 * a
       x2 = (-b - D**0.5) / 2 * a
       print("Ответ", float(x1), float(x2))
    else:
        if D == 0:
            x = -b / 2 * a
            print("Ответ",float(x))
        else: print("Корней нет")


