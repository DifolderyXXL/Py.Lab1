def format_rub(amount):
    return f"{amount:.2f} руб."

try:
    base_minutes = 60
    base_sms = 30
    base_data_mb = 1024
    base_price = 24.99

    extra_minute_price = 0.89
    extra_sms_price = 0.59
    extra_mb_price = 0.79
    tax_rate = 0.02

    used_minutes = int(input("Введите количество использованных минут: "))
    used_sms = int(input("Введите количество отправленных SMS: "))
    used_data_mb = int(input("Введите объем использованного интернет-трафика (в МБ): "))

    extra_minutes = max(0, used_minutes - base_minutes)
    extra_sms = max(0, used_sms - base_sms)
    extra_data_mb = max(0, used_data_mb - base_data_mb)

    extra_minutes_cost = extra_minutes * extra_minute_price
    extra_sms_cost = extra_sms * extra_sms_price
    extra_data_cost = extra_data_mb * extra_mb_price

    subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_data_cost

    tax = subtotal * tax_rate

    total = subtotal + tax

    print("\nРасчёт:")
    print(f"Базовая стоимость: {format_rub(base_price)}")

    if extra_minutes > 0:
        print(f"Доп. минуты ({extra_minutes} мин): {format_rub(extra_minutes_cost)}")
    if extra_sms > 0:
        print(f"Доп. SMS ({extra_sms} шт): {format_rub(extra_sms_cost)}")
    if extra_data_mb > 0:
        print(f"Доп. интернет ({extra_data_mb} МБ): {format_rub(extra_data_cost)}")

    print(f"Налог (2%): {format_rub(tax)}")
    print(f"Итоговая сумма к оплате: {format_rub(total)}")

except ValueError:
    print("Ошибка ввода")