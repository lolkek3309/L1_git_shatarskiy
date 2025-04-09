# Задача 1
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Ошибка: введено не число")

# Задача 2
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Файл не найден")