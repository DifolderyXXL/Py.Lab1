def checkIp(ip: str):
    parts = line.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True

line = input("Введите IP: ");

if checkIp(line):
    print("Correct")
else:
    print("Incorrect")




