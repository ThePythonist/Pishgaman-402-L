def check_duplication1(word):
    characters = ""
    for char in word:
        if char not in characters:
            characters += char
        else:
            return "Tekrari darad"

    return "Tekrari nadarad"


def check_duplication2(word):
    if len(set(word)) == len(word):
        return "Tekrari nadarad"
    else:
        return "Tekrari darad"


print(check_duplication2("aria"))
