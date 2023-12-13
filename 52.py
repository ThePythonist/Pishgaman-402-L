def is_perfect(number):
    divisors = []

    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    print(divisors)

    if number == sum(divisors):
        print(True)
    else:
        print(False)

is_perfect(28)
