import random
import datetime
import math

# Задача 1
print(random.randint(1, 100))

# Задача 2
print(datetime.datetime.now())

# Задача 3
def my_sqrt(number):
    guess = number / 2
    for _ in range(10):
        guess = (guess + number/guess) / 2
    return guess

print(math.sqrt(25))
print(my_sqrt(25))