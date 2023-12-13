def func(number):
    digits = [ int(i) for i in str(number) ]
    return sum(digits)


items = [415,2039,234,656,1111]

for i in items:
    print(func(i))
