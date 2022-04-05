num = int(input("Введите число от 2 до 10:"))
if 2 <= num <= 10:
    for num2 in range(1, 10):
        print("таблица умножения из числа num:", num * num2)
else:
    print("число не соответствует условию")
