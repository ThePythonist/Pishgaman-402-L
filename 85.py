lines = open("words.txt").read().split("\n")
has_digit = []

for i in lines:
    if not i.isdigit():
        for j in i:
            if j.isdigit():
                has_digit.append(i)
                break

print(has_digit)
