line = input("Enter your line: ")

remove_symbols = ['a', 'e', 'i', 'o', 'u']

for symbol in remove_symbols:
    line = line.replace(symbol, '')

print("Answer:", line)