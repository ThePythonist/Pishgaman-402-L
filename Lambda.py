# def f(name):
#     return "Hello" + " " + name
#
#
# print(f("nima"))
#
# greet = lambda name: "Hello" + " " + name
# print(greet("nima"))
#
#
# --------------------------------------------------------------------
#
#
# def power(x, y):
#     return x ** y
#
#
# print(power(4, 3))

# power = lambda x, y: x ** y
# print(power(2, 3))
#
#
# --------------------------------------------------------------------
#
#
# def f(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(f(4))
#
# f = lambda x: True if x % 2 == 0 else False
# print(f(8))


# --------------------------------------------------------------------
#
# print((lambda x, y: x + y)(5, 4))
#
# --------------------------------------------------------------------

if (lambda x: True if x % 2 == 0 else False)(13):
    print("Yes")
else:
    print("No")
