x = int(input("Enter any number : "))
divs = [i for i in range(1,x) if x % i == 0]
print((lambda x : True if x == sum(divs) else False)(x))
