#1
a = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

for index, element in enumerate(a):
    print(index, element)

#2
import random

start_guess = 0
number = random.randint(1, 20)

while start_guess  < 5:
    guess = int(input("Enter your number: "))
    start_guess += 1
    if guess < number:
        print("Слишком мало")
    elif guess > number:
        print("Слишком много")
if guess == number:
    print("Класс! Вы выиграли.")
else:
    print("Все, вы не выиграли. Игра завершилась")

#3
b = "adverts"
print(b[2:5])

#4
a = "Aidana"
b = "Adilet"

print(a.join(b)[:9])