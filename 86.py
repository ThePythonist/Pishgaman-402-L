number = int(input("How many files do you need ? "))
format = input("Which type of file do you need ? ")

for i in range(number):
    open(f"file{i+1}.{format}","w")

print("Done")
