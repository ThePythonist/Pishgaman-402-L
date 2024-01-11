users = [
    "09396908964",
    "09129232905",
    "09220878392",
]


def send_message(user):
    message = f"""
        Moshtarake gerami {user} shoma 85% az basteye khod ra masraf kardeid.
        """
    return message


m = list(map(send_message, users))
print(m)
