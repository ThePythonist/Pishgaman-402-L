balance = 0


def show_balance():
    print(balance)


show_balance()


def transaction(value):
    global balance
    balance += value


transaction(+500)
print(balance)
