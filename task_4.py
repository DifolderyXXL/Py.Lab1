

def print_ans(cnt: int, cupura: int) -> None:
    print(f"Понадобится {cnt} купюр по {cupura}")

def __main__():
    number = input("Введите сумму денег для размена: ")

    if not number.isdigit():
        print("Ошибка ввода, возможен ввод только чисел")
        return

    number = int(number)

    cupuras = [100, 50, 10, 5, 2, 1]

    for cupura in cupuras:
        print_ans(number//cupura, cupura)
        number %= cupura

__main__()