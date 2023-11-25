# entry = input("Type something : ")
#
# while entry != "exit":
#     print(entry)
#     entry = input("Type something : ")
# else :
#     print("Entry has turned into exit")

# ------------------------------------------------

flag = True

while flag:
    entry = input("Type something : ")
    if entry == "exit":
        # flag = False
        flag = 0
        # break
else:
    print("The flag has turned into False")
