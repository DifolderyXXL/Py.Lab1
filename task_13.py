from random import Random

rand = Random()

target = rand.randint(1, 100)
attempt = -1
while target != attempt:
    try:
        attempt = int(input("Введите число: "))
    except ValueError:
        print("Ошибка ввода!")
        continue

    if attempt < target:
        print(f"{attempt} < загаданного")
    elif attempt > target:
        print(f"{attempt} > загаданного")
    elif attempt == target:
        break;

print(f"Число угадано: {target}")
