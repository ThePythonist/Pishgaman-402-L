number = int(input("Enter any number : "))
numbers = [156, 122, 112, 994]

# if number % 2 == 0 and 99 < number < 1000:
if number % 2 == 0 and len(str(abs(number))) == 3:
    numbers.append(number)

print(numbers)
