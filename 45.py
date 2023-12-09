data = {
    "Model": "N552VW",
    "GPU": "GTX 960M",
    "Memory": "8GB DDR4",
    "Storage": {"SSD": "256", "HDD": "1TB"},
    "Display": "4K"
}

entry = input("Search anything : ")

# if entry in data:
#     print(data[entry])
# else:
#     print(entry, "Not Found")

try:
    print(data[entry])
except KeyError:
    print(entry, "Not Found")
