def newsort(items):
    items = list(items)
    items.sort()
    return items[::-1]


print(newsort([10, 5, 8, 7, 4, 2, 3]))
