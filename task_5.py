
def __main__():
    number = input("Введите число: ")

    if not number.isdigit():
        print("Ошибка ввода, возможен ввод только чисел")
        return

    number = int(number)

    if number % 7 == 0:
        print("Магическое число!")
    else:
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        print("ans:", sum)

__main__()