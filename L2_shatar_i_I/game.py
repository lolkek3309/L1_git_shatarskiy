import random

number = random.randint(0, 10)
attempts = 3

print("Угадайте число от 0 до 10!")

for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt+1}: "))

    if guess == number:
        print("Поздравляем! Вы угадали!")
        break
    elif guess < number:
        print("Загаданное число больше!")
    else:
        print("Загаданное число меньше!")
else:
    print(f"Вы проиграли! Число было: {number}")