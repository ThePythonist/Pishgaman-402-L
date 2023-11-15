data = {
    "class": "L",
    "teacher": "Sadeghi",
    "students": [{"name": "aria", "age": 17}, {"name": "hassan", "age": 30}, {"name": "tara", "age": 20}],
    "academy": "Pishgaman Sanaat"
}

timeofclass = {
    "days": ["shanbe", "4shanbe"],
    "times": ["17:00", "17:00"]
}

data.update(timeofclass)
# print(data)
print(data["students"][2]["age"])
