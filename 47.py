scores = {
    "mabani computer": 20,
    "riazi1": 15,
    "zaban": 18,
    "andishe1": 7,
    "madar manteghi": 20,
    "sakhteman dade": 14
}

for k,v in scores.items():
    if v >= 10 :
        print(k,": Passed")
    else :
        print(k,": Failed")

average = sum(scores.values()) / len(scores)
print(average)
