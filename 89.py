import random
def generate_password():
    password = ""

    for i in range(6):
        # password += str(random.randint(0,9))
        password += str(random.choice(range(0,10)))

    return password


print(generate_password())
