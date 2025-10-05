def getZodiac(day, month):
    zodiacDates = {
        (1, 20): "Водолей",
        (2, 19): "Рыбы",
        (3, 21): "Овен",
        (4, 20): "Телец",
        (5, 21): "Близнецы",
        (6, 21): "Рак",
        (7, 23): "Лев",
        (8, 23): "Дева",
        (9, 23): "Весы",
        (10, 23): "Скорпион",
        (11, 22): "Стрелец",
        (12, 22): "Козерог"
    }

    for (m, d), sign in zodiacDates.items():
        if (month, day) < (m, d):
            return prevSign
        prevSign = sign
    return prevSign

try:
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))

    if day < 1 or day > 31:
        raise ValueError("Неверное значение дня")
    if month < 1 or month > 12:
        raise ValueError("Неверное значение месяца")

    print(f"Ваш знак зодиака: {getZodiac(day, month)}")
except ValueError:
    print("Ошибка ввода")


