data = {
    "mabani computer": (20, 3),
    "riazi1": (15, 3),
    "zaban": (18, 2),
    "andishe1": (7, 1),
    "madar manteghi": (20, 3),
    "sakhteman dade": (14, 2)
}


def ghaboli(scores):
    for k, v in scores.items():
        if v[0] * v[1] >= 10:
            print(k, ": Passed")
        else:
            print(k, ": Failed")


def moadel(scores):
    nomarat = []
    zarayeb = []
    for i in scores.values():
        nomarat.append(i[0] * i[1])
        zarayeb.append(i[1])

    print()
    print("moadel :", sum(nomarat) / sum(zarayeb))


# -----------------------------------

ghaboli(data)
moadel(data)
