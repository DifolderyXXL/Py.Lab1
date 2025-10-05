lastname = input("Enter your last name: ")
firstname = input("Enter your first name: ")
surname = input("Enter your sur name: ")

lastname = lastname.lower().capitalize()
firstname = firstname.lower().capitalize()
surname = surname.lower().capitalize()

print(lastname + " " + firstname[0] + "." + surname[0] + '.')