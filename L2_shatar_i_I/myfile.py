# Задача 1
with open("test.txt", "w") as f:
    f.write("Hello, File!")

# Задача 2
with open("test.txt", "r") as f:
    print(f.read())

# Задача 3
with open("test.txt", "a") as f:
    f.write("\nНовая строка")