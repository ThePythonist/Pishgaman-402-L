txt = "python is a good programming language"


def find_longest1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    maxlen = max(lengths)

    for i in text:
        if len(i) == maxlen:
            print(i)


def find_longest2(text):
    text = text.split()
    text.sort(key=len)
    print(text[-1])


def find_longest3(text):
    text = text.split()
    print(max(text, key=len))


find_longest3(txt)
