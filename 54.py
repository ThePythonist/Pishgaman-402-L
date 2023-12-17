# def check1(numbers):
#     characters = {"0", "1"}
#     binaries = []
#     for number in numbers:
#         for char in number:
#             if char not in characters:
#                 break
#         else:
#             binaries.append(number)
#
#     print(binaries)
#
#
# check1(["24", "11101", "1111", "10101", "105"])

def check2(numbers):
    characters = {"0", "1"}
    binaries = []
    for number in numbers:
        for char in number:
            if char not in characters:
                break
        else:
            binaries.append(number)

    print(binaries)


items = ["24", "11101", "1111", "10101", "105"]
check2(items)