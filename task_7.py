def calculate():
    try:
        seconds = int(input())
        minutes = seconds // 60
        seconds = seconds % 60
        print(f"{minutes} минут {seconds} секунд.")

    except ValueError:
        print("Требуется ввести число")


calculate()