entry = input("Type something : ")
numbers = []

while entry != "exit":
    entry = input("Type something : ")
    try:
        entry = float(entry)
        if str(entry)[-2:] == ".0":
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        # print("Entry is not a number")
        pass

print(numbers)
