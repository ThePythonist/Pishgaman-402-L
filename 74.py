lines = open("words.txt").readlines()

for i in lines[:50] :
    if len(i) == 6 :
        print(i)

