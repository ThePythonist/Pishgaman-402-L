# def check_prime(number):
#     divisors = [ i for i in range(1,number+1) if number % i == 0]
#     print(True) if len(divisors) == 2 else print(False)
#
#
# number = int(input("Enter any number : "))
# check_prime(number)

def check_prime(number):
    divisors = [ i for i in range(1,number+1) if number % i == 0]
    return True if len(divisors) == 2 else False


number = int(input("Enter any number : "))
print(check_prime(number))
