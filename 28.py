a = 0
b = 1

# for i in range(100):
#     print(a)
#     c = a
#     a = b
#     b = c+b


for i in range(100):
    print(a)
    a, b = b, a + b
