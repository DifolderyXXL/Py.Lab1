line = input("Введите строку: ")

verdict = 1
for i in range(line.__len__() // 2):
    verdict &= line[i] == line[line.__len__() - 1 - i]

if verdict == 1:
    print("Палиндром")
else:
    print("Не палиндром")