# def divisors(x):
#     return [i for i in range(1, x + 1) if x % i == 0]
#
#
# numbers = []
# for i in range(3):
#     numbers.append(int(input("Enter number : ")))
#
# print(list(map(divisors, numbers)))

# -----------------------------------------------------------------

numbers = [int(input("Enter number : ")) for i in range(4)]
print(list(map(lambda x: [i for i in range(1,x+1) if x % i == 0], numbers)))
