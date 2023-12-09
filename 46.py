ages = {
    "behnam":30,
    "arad":14,
    "kian":40,
    "sepehr":18,
    "ariana":23,
    "meysam":40,
    "aysa":25
}

maxage = max(ages.values())

for i in ages:
    if ages[i] == maxage:
        print(i)
