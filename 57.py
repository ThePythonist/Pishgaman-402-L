def evenorodd(number):
    if number % 2 == 0 :
        print("Even")
    else :
        print("Odd")


def is_number(entry):
    if entry.isdigit():
        evenorodd(int(entry))
    else:
        print("Entry must be a number")
        is_number(input("Enter any number : "))


is_number(input("Enter any number : "))
