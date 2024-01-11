lines = open("words.txt").readlines()
five_letters = []

for i in lines[:50]:
    if len(i) == 6:
        five_letters.append(i)

open("5_letters.txt","w").writelines(five_letters)
