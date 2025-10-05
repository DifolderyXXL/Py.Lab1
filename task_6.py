def calculate_moles():
    print("Введите значения в следующих единицах:")
    print("Давление (Па), Объем (м³), Температура (К)")

    try:
        pressure = float(input("Давление (Па): "))
        volume = float(input("Объем (м³): "))
        temperature = float(input("Температура (К): "))

        R = 8.314
        moles = (pressure * volume) / (R * temperature)

        print(f"Количество вещества: {moles:.6f} моль")
    except ValueError:
        print("Ошибка: пожалуйста, введите числовые значения.")

calculate_moles()
