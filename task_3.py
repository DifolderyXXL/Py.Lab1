password = input("Enter your password: ")

if password.__len__() < 16:
    print("Слишком короткий")
elif password.isdigit() or password.isalpha():
    print("Слабый пароль")
else:
    print("Надежный пароль")