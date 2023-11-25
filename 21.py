# word = input("Enter any word : ")
# mytuple = ("dad", "nan", "mom")
#
# if word == word[::-1]:
#     mytuple = list(mytuple)
#     mytuple.append(word)
#
# mytuple = tuple(mytuple)
# print(mytuple)

# ---------------------------------------------

word = input("Enter any word : ")
mytuple = ("dad", "nan", "mom")

if word == word[::-1]:
    mytuple += (word,)


print(mytuple)
